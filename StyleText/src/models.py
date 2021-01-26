import torch
import torch.nn as nn
from torch.nn import Linear, Conv2d, BatchNorm2d, LeakyReLU, ConvTranspose2d, ReLU, Tanh, InstanceNorm2d, \
    ReplicationPad2d
import torch.nn.functional as F
import random
from utils import gaussian, to_var, to_data, save_image, tensor2pil, pil2tensor
from vgg import GramMSELoss, SemanticFeature
import numpy as np
import math
import torch.autograd as autograd
from torch.autograd import Variable
import os
import cv2 as cv
from PIL import Image
id = 0  # for saving network output to file during training


#######################  Texture Network
# based on Convolution-BatchNorm-ReLU
class myTConv(nn.Module):
    def __init__(self, num_filter=128, stride=1, in_channels=128):
        super(myTConv, self).__init__()

        self.pad = ReplicationPad2d(padding=1)
        self.conv = Conv2d(out_channels=num_filter, kernel_size=3,
                           stride=stride, padding=0, in_channels=in_channels)
        self.bn = BatchNorm2d(num_features=num_filter, track_running_stats=True)
        self.relu = ReLU()

    def forward(self, x):
        return self.relu(self.bn(self.conv(self.pad(x))))


class myTBlock(nn.Module):
    def __init__(self, num_filter=128, p=0.0):
        super(myTBlock, self).__init__()

        self.myconv = myTConv(num_filter=num_filter, stride=1, in_channels=128)
        self.pad = ReplicationPad2d(padding=1)
        self.conv = Conv2d(out_channels=num_filter, kernel_size=3, padding=0, in_channels=128)
        self.bn = BatchNorm2d(num_features=num_filter, track_running_stats=True)
        self.relu = ReLU()
        self.dropout = nn.Dropout(p=p)

    def forward(self, x):
        return self.dropout(self.relu(x + self.bn(self.conv(self.pad(self.myconv(x))))))


class TextureGenerator(nn.Module):
    def __init__(self, ngf=32, n_layers=5):
        """

        :param ngf: 32
        :param n_layers: 6
        """
        super(TextureGenerator, self).__init__()

        modelList = []
        modelList.append(ReplicationPad2d(padding=4))
        modelList.append(Conv2d(out_channels=ngf, kernel_size=9, padding=0, in_channels=3))
        modelList.append(ReLU())
        modelList.append(myTConv(ngf * 2, 2, ngf))
        modelList.append(myTConv(ngf * 4, 2, ngf * 2))

        for n in range(int(n_layers / 2)):  # 0 1 2
            modelList.append(myTBlock(ngf * 4, p=0.0))
        # dropout to make model more robust
        modelList.append(myTBlock(ngf * 4, p=0.5))
        for n in range(int(n_layers / 2) + 1, n_layers):  # 4 5
            modelList.append(myTBlock(ngf * 4, p=0.0))

        modelList.append(ConvTranspose2d(out_channels=ngf * 2, kernel_size=4, stride=2, padding=0, in_channels=ngf * 4))
        modelList.append(BatchNorm2d(num_features=ngf * 2, track_running_stats=True))
        modelList.append(ReLU())
        modelList.append(ConvTranspose2d(out_channels=ngf, kernel_size=4, stride=2, padding=0, in_channels=ngf * 2))
        modelList.append(BatchNorm2d(num_features=ngf, track_running_stats=True))
        modelList.append(ReLU())
        modelList.append(ReplicationPad2d(padding=1))
        modelList.append(Conv2d(out_channels=3, kernel_size=9, padding=0, in_channels=ngf))
        modelList.append(Tanh())
        self.model = nn.Sequential(*modelList)

    def forward(self, x):
        return self.model(x)


###################### Glyph Network
# based on Convolution-BatchNorm-LeakyReLU
class myGConv(nn.Module):
    def __init__(self, num_filter=128, stride=1, in_channels=128):
        super(myGConv, self).__init__()
        self.pad = ReplicationPad2d(padding=1)
        self.conv = Conv2d(out_channels=num_filter, kernel_size=3,
                           stride=stride, padding=0, in_channels=in_channels)
        self.bn = BatchNorm2d(num_features=num_filter, track_running_stats=True)
        # either ReLU or LeakyReLU is OK
        self.relu = LeakyReLU(0.2)

    def forward(self, x):
        return self.relu(self.bn(self.conv(self.pad(x))))


class myGBlock(nn.Module):
    def __init__(self, num_filter=128):
        super(myGBlock, self).__init__()

        self.myconv = myGConv(num_filter=num_filter, stride=1, in_channels=num_filter)
        self.pad = ReplicationPad2d(padding=1)
        self.conv = Conv2d(out_channels=num_filter, kernel_size=3, padding=0, in_channels=num_filter)
        self.bn = BatchNorm2d(num_features=num_filter, track_running_stats=True)

    def forward(self, x):
        return x + self.bn(self.conv(self.pad(self.myconv(x))))


# 可控的 ResBlock
# Controllable ResBlock
class myGCombineBlock(nn.Module):
    def __init__(self, num_filter=128, p=0.0):
        super(myGCombineBlock, self).__init__()

        self.myBlock1 = myGBlock(num_filter=num_filter)
        self.myBlock2 = myGBlock(num_filter=num_filter)
        self.relu = LeakyReLU(0.2)
        self.label = 1.0  # 初始化
        self.dropout = nn.Dropout(p=p)

    def myCopy(self):
        self.myBlock1.load_state_dict(self.myBlock2.state_dict())

    def forward(self, x):
        return self.dropout(self.relu(self.myBlock1(x) * self.label + self.myBlock2(x) * (1.0 - self.label)))


class GlyphGenerator(nn.Module):
    def __init__(self, ngf=32, n_layers=5):
        """
        训练结构时：
        :param ngf: 32
        :param n_layers: 6!!!
        """
        super(GlyphGenerator, self).__init__()

        encoder = []
        encoder.append(ReplicationPad2d(padding=4))
        encoder.append(Conv2d(out_channels=ngf, kernel_size=9, padding=0, in_channels=3))
        encoder.append(LeakyReLU(0.2))
        encoder.append(myGConv(ngf * 2, 2, ngf))
        encoder.append(myGConv(ngf * 4, 2, ngf * 2))

        transformer = []
        for n in range(int(n_layers / 2) - 1):  # 0,1
            transformer.append(myGCombineBlock(ngf * 4, p=0.0))
        # dropout to make model more robust
        transformer.append(myGCombineBlock(ngf * 4, p=0.5))
        transformer.append(myGCombineBlock(ngf * 4, p=0.5))
        for n in range(int(n_layers / 2) + 1, n_layers):
            transformer.append(myGCombineBlock(ngf * 4, p=0.0))

        decoder = []
        decoder.append(ConvTranspose2d(out_channels=ngf * 2, kernel_size=4, stride=2, padding=0, in_channels=ngf * 4))
        decoder.append(BatchNorm2d(num_features=ngf * 2, track_running_stats=True))
        decoder.append(LeakyReLU(0.2))
        decoder.append(ConvTranspose2d(out_channels=ngf, kernel_size=4, stride=2, padding=0, in_channels=ngf * 2))
        decoder.append(BatchNorm2d(num_features=ngf, track_running_stats=True))
        decoder.append(LeakyReLU(0.2))
        decoder.append(ReplicationPad2d(padding=1))
        decoder.append(Conv2d(out_channels=3, kernel_size=9, padding=0, in_channels=ngf))
        decoder.append(Tanh())

        self.encoder = nn.Sequential(*encoder)
        self.transformer = nn.Sequential(*transformer)
        self.decoder = nn.Sequential(*decoder)

    def myCopy(self):
        for myCombineBlock in self.transformer:
            myCombineBlock.myCopy()

    # controlled by Controllable ResBlcok
    def forward(self, x, l):
        for myCombineBlock in self.transformer:
            # label smoothing [-1,1]-->[0.9,0.1]
            myCombineBlock.label = (1.0 - l) * 0.4 + 0.1
            # [-1, -0.333, 0.333, 1]-->[0.9, 0.6333333333333334, 0.3666666666666667, 0.1]
        out0 = self.encoder(x)  # out0: [32, 128, 64, 64]
        out1 = self.transformer(out0)
        out2 = self.decoder(out1)
        return out2


##################### Sketch Module
# based on Convolution-InstanceNorm-ReLU
# Smoothness Block
class myBlur(nn.Module):
    def __init__(self, kernel_size=121, channels=3):
        super(myBlur, self).__init__()
        kernel_size = int(int(kernel_size / 2) * 2) + 1  # 结果 121
        self.kernel_size = kernel_size  # 121
        self.channels = channels  # 3
        # TODO 这个 GF 没有看到那里用到
        self.GF = nn.Conv2d(in_channels=channels, out_channels=channels,
                            kernel_size=kernel_size, groups=channels, bias=False)
        x_cord = torch.arange(self.kernel_size + 0.)  # 0.0到120.0包括120.0的浮点数，step=1.0
        x_grid = x_cord.repeat(self.kernel_size).view(self.kernel_size, self.kernel_size)  # 121*121的张量，每个是一个x_cord
        y_grid = x_grid.t()  # 转置
        self.xy_grid = torch.stack([x_grid, y_grid], dim=-1)  # -1就是最后那一维，结果size为 121,121,2

        self.mean = (self.kernel_size - 1) // 2  # 结果是 60

        self.diff = -torch.sum((self.xy_grid - self.mean) ** 2., dim=-1)


        self.gaussian_filter = nn.Conv2d(in_channels=self.channels, out_channels=self.channels,
                                         kernel_size=self.kernel_size, groups=self.channels, bias=False)
        # 权重无需学习，见下面的forward
        self.gaussian_filter.weight.requires_grad = False

    def forward(self, x, sigma, gpu):
        sigma = sigma * 8. + 16.
        variance = sigma ** 2.
        gaussian_kernel = (1. / (2. * math.pi * variance)) * torch.exp(self.diff / (2 * variance))
        # print(f'myBlur forward diff: {self.diff}')
        gaussian_kernel = gaussian_kernel / torch.sum(gaussian_kernel)
        # print(f'myBlur forward gaussian_kernel.shape {gaussian_kernel.shape}')  # [121, 121]
        gaussian_kernel = gaussian_kernel.view(1, 1, self.kernel_size, self.kernel_size)
        gaussian_kernel = gaussian_kernel.repeat(self.channels, 1, 1, 1)
        if gpu:
            gaussian_kernel = gaussian_kernel.cuda()
        # self.gaussian_filter 的权重直接设为 gaussian_kernel，根据sigma(l)来的
        # print(f'myBlur forward {gaussian_kernel}')
        # print(f'myBlur forward {gaussian_kernel.shape}')
        # print(f'myBlur forward {self.gaussian_filter}')
        self.gaussian_filter.weight.data = gaussian_kernel
        return self.gaussian_filter(F.pad(x, (self.mean, self.mean, self.mean, self.mean), "replicate"))


class myErode(nn.Module):
    def __init__(self, kernel_size=2):
        super(myErode, self).__init__()
        self.erode_kernel = kernel_size

    def forward(self, x, l, gpu):
        iterations_times = int(4 * (l + 2 - 1))
        kernel = np.ones((self.erode_kernel + 2 * iterations_times, self.erode_kernel + 2 * iterations_times), np.uint8)
        # print(l)
        # OpenCV是BGR的！！！
        eroded_lst = []
        for e in x:
            x_pil = tensor2pil(e.cpu() * 0.5 + 0.5)
            eroded_tensor = pil2tensor(Image.fromarray(cv.erode(np.asarray(x_pil), kernel, iterations=1)))
            eroded_lst.append(eroded_tensor.unsqueeze(dim=0))

        x = torch.cat(eroded_lst, dim=0)
        # print(f'-myErode forward:{x.shape}')
        if gpu:
            x = x.to('cuda')
        return x



class mySConv(nn.Module):
    def __init__(self, num_filter=128, stride=1, in_channels=128):
        super(mySConv, self).__init__()

        self.conv = Conv2d(out_channels=num_filter, kernel_size=3,
                           stride=stride, padding=1, in_channels=in_channels)
        self.bn = InstanceNorm2d(num_features=num_filter)
        self.relu = ReLU()

    def forward(self, x):
        return self.relu(self.bn(self.conv(x)))


class mySBlock(nn.Module):
    def __init__(self, num_filter=128):
        super(mySBlock, self).__init__()
        # 在SketchModel的transformer里，num_filter是129
        self.myconv = mySConv(num_filter=num_filter, stride=1, in_channels=num_filter)
        self.conv = Conv2d(out_channels=num_filter, kernel_size=3, padding=1, in_channels=num_filter)
        self.bn = InstanceNorm2d(num_features=num_filter)
        self.relu = ReLU()

    def forward(self, x):
        return self.relu(x + self.bn(self.conv(self.myconv(x))))


# Transformation Block
# 变形块
class SketchGenerator(nn.Module):
    def __init__(self, in_channels=4, ngf=32, n_layers=5):
        """
        生成器
        :param in_channels: 传入的是 4
        :param ngf: 生成器第一层的特征的数量 传入的是 32
        :param n_layers: 生成器的网络的层数 传入的是 6
        """
        super(SketchGenerator, self).__init__()

        encoder = []
        encoder.append(Conv2d(in_channels=in_channels, out_channels=ngf, kernel_size=9, padding=4))
        encoder.append(ReLU())
        encoder.append(mySConv(ngf * 2, 2, ngf))
        encoder.append(mySConv(ngf * 4, 2, ngf * 2))

        transformer = []
        for n in range(n_layers):  # n_layers: 生成器的网络的层数
            transformer.append(mySBlock(ngf * 4 + 1))  # TODO 额外加 1？？？

        decoder1 = []
        decoder2 = []
        decoder3 = []
        decoder1.append(ConvTranspose2d(
            out_channels=ngf * 2,
            kernel_size=4, stride=2, padding=0,
            in_channels=ngf * 4 + 2))  # 为什么加 2？？？
        decoder1.append(InstanceNorm2d(num_features=ngf * 2))
        decoder1.append(ReLU())

        decoder2.append(ConvTranspose2d(
            out_channels=ngf,
            kernel_size=4, stride=2, padding=0,
            in_channels=ngf * 2 + 1))  # 为什么加 1？？？
        decoder2.append(InstanceNorm2d(num_features=ngf))
        decoder2.append(ReLU())

        decoder3.append(Conv2d(out_channels=3, kernel_size=9, padding=1, in_channels=ngf + 1))
        decoder3.append(Tanh())

        self.encoder = nn.Sequential(*encoder)
        self.transformer = nn.Sequential(*transformer)
        self.decoder1 = nn.Sequential(*decoder1)
        self.decoder2 = nn.Sequential(*decoder2)
        self.decoder3 = nn.Sequential(*decoder3)

    # controlled by label concatenation
    def forward(self, x, l):
        l_img = l.expand(l.size(0), l.size(1), x.size(2), x.size(3))
        # print(f'+encoder:x:{x.shape};l_img:{l_img.shape}')  # [16, 3, 256, 256] , [16, 1, 256, 256]
        out0 = self.encoder(torch.cat([x, l_img], 1))  # [16, 3, 256, 256] cat [16, 1, 256, 256] = [16, 4, 256, 256]
        # print(f'-encoder:out0:{out0.shape}')  # out0: [16, 128, 64, 64]
        #         print(torch.cat([x, l_img], 1)[0,3,:,:])  # 值都是0.25

        l_img0 = l.expand(l.size(0), l.size(1), out0.size(2), out0.size(3))
        # print(f'+transformer:l_img0:{l_img0.shape}')  # [16, 1, 64, 64]
        out1 = self.transformer(torch.cat([out0, l_img0], 1))
        # out0: [16, 128, 64, 64] cat l_img0:[16, 1, 64, 64] = [16, 129, 64, 64]
        # print(f'-transformer:out1:{out1.shape}')  # [16, 129, 64, 64]

        l_img1 = l.expand(l.size(0), l.size(1), out1.size(2), out1.size(3))
        # print(f'+decoder1:l_img1:{l_img1.shape}')  # [16, 1, 64, 64]
        out2 = self.decoder1(torch.cat([out1, l_img1], 1))  # [16, 129, 64, 64] cat [16, 1, 64, 64] = [16, 130, 64, 64]
        # print(f'-decoder1:out2:{out2.shape}')  # [16, 64, 130, 130]

        l_img2 = l.expand(l.size(0), l.size(1), out2.size(2), out2.size(3))
        # print(f'+decoder2:l_img2:{l_img2.shape}')  # [16, 1, 130, 130]
        out3 = self.decoder2(torch.cat([out2, l_img2], 1))
        # print(f'-decoder2:out3:{out3.shape}')  # [16, 32, 262, 262]

        l_img3 = l.expand(l.size(0), l.size(1), out3.size(2), out3.size(3))
        # print(f'+decoder3:l_img3:{l_img3.shape}')  # [16, 1, 262, 262]
        out4 = self.decoder3(torch.cat([out3, l_img3], 1))
        # print(f'-decoder3:out4:{out4.shape}')  # [16, 3, 256, 256]
        return out4


################ Discriminators
# Glyph and Texture Networks: BN
# Sketch Module: IN, multilayer
class Discriminator(nn.Module):  # 使用的是Pix2Pix中提出的判别器--PatchGAN
    def __init__(self, in_channels, ndf=32, n_layers=3, multilayer=False, IN=False):
        """
        Sketch Module时:
        :param in_channels: 7
        :param ndf: 32
        :param n_layers: 5
        :param multilayer: True
        :param IN: True
        """
        super(Discriminator, self).__init__()

        modelList = []
        outlist1 = []
        outlist2 = []
        kernel_size = 4
        padding = int(np.ceil((kernel_size - 1) / 2))  # 训练SketchModule时是 2,向大数取整
        modelList.append(Conv2d(out_channels=ndf, kernel_size=kernel_size, stride=2,
                                padding=2, in_channels=in_channels))
        modelList.append(LeakyReLU(0.2))

        nf_mult = 1
        for n in range(1, n_layers):  # 训练SketchModule时是 1,2,3,4，训练Structure时是1,2,3
            nf_mult_prev = nf_mult
            nf_mult = min(2 ** n, 4)
            modelList.append(Conv2d(out_channels=ndf * nf_mult, kernel_size=kernel_size, stride=2,
                                    padding=2, in_channels=ndf * nf_mult_prev))
            if IN:
                modelList.append(InstanceNorm2d(num_features=ndf * nf_mult))
            else:
                modelList.append(BatchNorm2d(num_features=ndf * nf_mult, track_running_stats=True))
            modelList.append(LeakyReLU(0.2))

        nf_mult_prev = nf_mult
        nf_mult = min(2 ** n_layers, 4)  # 训练SketchModule时结果是 4 啊
        outlist1.append(Conv2d(out_channels=1, kernel_size=kernel_size, stride=1,
                               padding=padding, in_channels=ndf * nf_mult_prev))

        outlist2.append(Conv2d(out_channels=ndf * nf_mult, kernel_size=kernel_size, stride=1,
                               padding=padding, in_channels=ndf * nf_mult_prev))
        if IN:
            outlist2.append(InstanceNorm2d(num_features=ndf * nf_mult))
        else:
            outlist2.append(BatchNorm2d(num_features=ndf * nf_mult, track_running_stats=True))
        outlist2.append(LeakyReLU(0.2))
        outlist2.append(Conv2d(out_channels=1, kernel_size=kernel_size, stride=1,
                               padding=padding, in_channels=ndf * nf_mult))
        self.model = nn.Sequential(*modelList)
        self.out1 = nn.Sequential(*outlist1)
        self.out2 = nn.Sequential(*outlist2)
        self.multilayer = multilayer  # 训练SketchModule时传入的是True

    def forward(self, x):
        y = self.model(x)  # sketch时 y.shape:[bs,128,9,9]；structure时 y.shape:[bs,128,17,17]
        out2 = self.out2(y)  # sketch时 out2.shape:[bs,1,11,11]；structure时[bs,1,19,19]
        if self.multilayer:  # 训练SketchModule时传入的是True;structure时False
            out1 = self.out1(y)  # out1:[bs,1,10,10]
            return torch.cat((out1.view(-1), out2.view(-1)), dim=0)  # 拼接两个向量，前半个是out1.view(-1)，后半个是out2.view(-1)
        else:
            return out2.view(-1)  # 变成向量


######################## Sketch Module 草图模块
class SketchModule(nn.Module):
    def __init__(self, G_layers=6, D_layers=5, ngf=32, ndf=32, gpu=True):
        super(SketchModule, self).__init__()

        self.G_layers = G_layers  # 生成器的层数 传入的 6
        self.D_layers = D_layers  # 判别器的层数 传入的 5
        self.ngf = ngf  # 生成器第一层的特征的数量 传入的 32
        self.ndf = ndf  # 判别器第一层的特征的数量 传入的 32
        self.gpu = gpu
        self.lambda_l1 = 100
        self.lambda_gp = 10
        self.lambda_adv = 1
        self.loss = nn.L1Loss()

        # Ske模块由两部分组成：
        # Sketch Module = transformationBlock + smoothnessBlock

        # transformationBlock
        self.transBlock = SketchGenerator(4, self.ngf, self.G_layers)

        # D_B 学习去确定输入图像的真实性以及它是否与给定的平滑图像 (t_l ) ̅ 和参数 l 相匹配
        # 7， 32， 5，True，True
        self.D_B = Discriminator(7, self.ndf, self.D_layers, True, True)

        # smoothnessBlock
        self.smoothBlock = myBlur()
        # self.smoothBlock = myErode()

        self.trainerG = torch.optim.Adam(self.transBlock.parameters(), lr=0.0002, betas=(0.5, 0.999))
        self.trainerD = torch.optim.Adam(self.D_B.parameters(), lr=0.0002, betas=(0.5, 0.999))

    # FOR TESTING
    def forward(self, t, l):
        l = torch.tensor(l).float()
        tl = self.smoothBlock(t, l, self.gpu)
        label = l.repeat(1, 1, 1, 1)
        label = label.cuda() if self.gpu else label
        return self.transBlock(tl, label)

    # FOR TRAINING
    # init weight
    def init_networks(self, weights_init):
        self.transBlock.apply(weights_init)
        self.D_B.apply(weights_init)

    # WGAN-GP: calculate gradient penalty
    def calc_gradient_penalty(self, netD, real_data, fake_data):
        alpha = torch.rand(real_data.shape[0], 1, 1, 1)
        alpha = alpha.cuda() if self.gpu else alpha

        interpolates = alpha * real_data + ((1 - alpha) * fake_data)
        interpolates = Variable(interpolates, requires_grad=True)

        disc_interpolates = netD(interpolates)

        gradients = autograd.grad(outputs=disc_interpolates, inputs=interpolates,
                                  grad_outputs=torch.ones(disc_interpolates.size()).cuda()
                                  if self.gpu else torch.ones(disc_interpolates.size()),
                                  create_graph=True, retain_graph=True, only_inputs=True)[0]

        gradient_penalty = ((gradients.norm(2, dim=1) - 1) ** 2).mean()
        return gradient_penalty

    def update_discriminator(self, t, l):
        label = torch.tensor(l).float()  # scale值变为张量
        label = label.repeat(t.size(0), 1, 1, 1)  # [batch_size, 1, 1, 1]
        label = to_var(label) if self.gpu else label

        real_label = label.expand(label.size(0), label.size(1), t.size(2), t.size(3))  # [16, 1, 256, 256]

        with torch.no_grad():
            # tl: 模糊度为 l 的16个图片张量
            tl = self.smoothBlock(t, l, self.gpu)  # tl [16, 3, 256, 256]
            # transBlock：将平滑后的文本图像 tl 映射回文本域以学习字形特征来实现结构转换
            fake_text = self.transBlock(tl, label)  # fake_text [16, 3, 256, 256]
            # print(tl.size(), real_label.size(), fake_text.size())
            fake_concat = torch.cat((tl, real_label, fake_text), dim=1)
            # fake_concat: [16, 7, 256, 256]

        fake_output = self.D_B(fake_concat)  # 3536维度的向量

        real_concat = torch.cat((tl, real_label, t), dim=1)
        # real_concat: [16, 7, 256, 256]
        real_output = self.D_B(real_concat)  # 一个3536维度的向量

        gp = self.calc_gradient_penalty(self.D_B, real_concat.data, fake_concat.data)
        # lambda_adv = 1, lambda_gp = 10
        LBadv = self.lambda_adv * (fake_output.mean() - real_output.mean() + self.lambda_gp * gp)

        self.trainerD.zero_grad()
        LBadv.backward()
        self.trainerD.step()
        return (real_output.mean() - fake_output.mean()).data.mean() * self.lambda_adv

    def update_generator(self, t, l):
        label = torch.tensor(l).float()
        label = label.repeat(t.size(0), 1, 1, 1)  # [16,1,1,1]
        label = label.cuda() if self.gpu else label
        # expand方法使用与扩展 1-dim 的张量，可以少用内存
        real_label = label.expand(label.size(0), label.size(1), t.size(2), t.size(3))  # [16, 1, 256, 256]

        tl = self.smoothBlock(t, l, self.gpu)

        fake_text = self.transBlock(tl, label)

        fake_concat = torch.cat((tl, real_label, fake_text), dim=1)
        # fake_concat: [16, 7, 256, 256]
        fake_output = self.D_B(fake_concat)  # 一个3536维度的向量

        LBadv = -fake_output.mean() * self.lambda_adv  # 对抗损失
        """
        https://zhuanlan.zhihu.com/p/263692012
        用于图像转换问题时，输入换成了一张图像，并引入了像素级别的L1或L2损失。像素级损失是逐像素地测量输出和真实图像之间的不一致性（颜色空间层面），而对抗损失测量的是输出和真实样本集间的似然度。
        """
        LBrec = self.loss(fake_text, t) * self.lambda_l1  # L1 Loss直接比较转换后的文本与原文本，没有经过判别器的！！！
        LB = LBadv + LBrec

        self.trainerG.zero_grad()
        LB.backward()
        self.trainerG.step()
        # global id
        # if id % 50 == 0:
        #    viz_img = to_data(torch.cat((t[0], tl[0], fake_text[0]), dim=2))
        #    save_image(viz_img, '../output/deblur_result%d.jpg'%id)
        # id += 1
        return LBadv.data.mean(), LBrec.data.mean()

    def one_pass(self, t, scales):
        """
        训练G_B的时候：
        :param t: shape为[batch_size, 3, 256, 256])
        :param scales: 值为[-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0]
        :return:
        """
        l = random.choice(scales)  # 从scales随机选择一个值
        LDadv = self.update_discriminator(t, l)
        LGadv, Lrec = self.update_generator(t, l)
        return [LDadv, LGadv, Lrec]


######################## ShapeMatchingGAN
class ShapeMatchingGAN(nn.Module):
    def __init__(self, GS_nlayers=6, DS_nlayers=5, GS_nf=32, DS_nf=32,
                 GT_nlayers=6, DT_nlayers=5, GT_nf=32, DT_nf=32, gpu=True):
        """
        :param GS_nlayers: 6
        :param DS_nlayers: 4
        :param GS_nf: 32
        :param DS_nf: 32
        :param GT_nlayers: 6
        :param DT_nlayers: 4
        :param GT_nf: 32
        :param DT_nf: 32
        :param gpu:
        """
        super(ShapeMatchingGAN, self).__init__()

        self.GS_nlayers = GS_nlayers  # 6
        self.DS_nlayers = DS_nlayers  # 4
        self.GS_nf = GS_nf  # 32
        self.DS_nf = DS_nf  # 32
        self.GT_nlayers = GT_nlayers  # 6
        self.DT_nlayers = DT_nlayers  # 4
        self.GT_nf = GT_nf  # 32
        self.DT_nf = DT_nf  # 32
        self.gpu = gpu
        self.lambda_l1 = 100
        self.lambda_gp = 10
        self.lambda_distance = 0.01
        self.lambda_sadv = 0.1
        self.lambda_gly = 1.0
        self.lambda_tadv = 1.0
        self.lambda_sty = 0.01
        self.style_weights = [1e3 / n ** 2 for n in [64, 128, 256, 512, 512]]
        # [0.244140625, 0.06103515625, 0.0152587890625, 0.003814697265625, 0.003814697265625]
        self.loss = nn.L1Loss()
        self.gramloss = GramMSELoss()
        self.gramloss = self.gramloss.cuda() if self.gpu else self.gramloss
        self.getmask = SemanticFeature()
        for param in self.getmask.parameters():
            param.requires_grad = False

        self.G_S = GlyphGenerator(self.GS_nf, self.GS_nlayers)
        self.D_S = Discriminator(3, self.DS_nf, self.DS_nlayers)
        self.G_T = TextureGenerator(self.GT_nf, self.GT_nlayers)
        self.D_T = Discriminator(6, self.DT_nf, self.DT_nlayers)

        self.trainerG_S = torch.optim.Adam(self.G_S.parameters(), lr=0.0002, betas=(0.5, 0.999))
        self.trainerD_S = torch.optim.Adam(self.D_S.parameters(), lr=0.0002, betas=(0.5, 0.999))
        self.trainerG_T = torch.optim.Adam(self.G_T.parameters(), lr=0.0002, betas=(0.5, 0.999))
        self.trainerD_T = torch.optim.Adam(self.D_T.parameters(), lr=0.0002, betas=(0.5, 0.999))

    # FOR TESTING
    def forward(self, x, l):
        x[:, 0:1] = gaussian(x[:, 0:1], stddev=0.2)
        xl = self.G_S(x, l)
        xl[:, 0:1] = gaussian(xl[:, 0:1], stddev=0.2)
        return self.G_T(xl)

    # FOR TRAINING
    # init weight
    def init_networks(self, weights_init):
        self.G_S.apply(weights_init)
        self.D_S.apply(weights_init)
        self.G_T.apply(weights_init)
        self.D_T.apply(weights_init)

    # WGAN-GP: calculate gradient penalty
    def calc_gradient_penalty(self, netD, real_data, fake_data):
        alpha = torch.rand(real_data.shape[0], 1, 1, 1)
        alpha = alpha.cuda() if self.gpu else alpha

        interpolates = alpha * real_data + ((1 - alpha) * fake_data)
        interpolates = Variable(interpolates, requires_grad=True)

        disc_interpolates = netD(interpolates)

        gradients = autograd.grad(outputs=disc_interpolates, inputs=interpolates,
                                  grad_outputs=torch.ones(disc_interpolates.size()).cuda()
                                  if self.gpu else torch.ones(disc_interpolates.size()),
                                  create_graph=True, retain_graph=True, only_inputs=True)[0]

        gradient_penalty = ((gradients.norm(2, dim=1) - 1) ** 2).mean()
        return gradient_penalty

    def update_structure_discriminator(self, x, xl, l):
        # xl与x裁剪的坐标是相同的。
        # xl是加入了一些噪声的自Xl[idx]随机裁剪出的 32 个 大小为 256x256 的xl图像 [32, 3, 256, 256]
        # x就是输入的Output的随机裁剪/选择后的结果，也就是原距离图像随机裁剪/选择后的，与 xl shape 相同 [32, 3, 256, 256]
        with torch.no_grad():
            fake_x = self.G_S(xl, l)  # shape同 x，是[32,3,256,256]
        fake_output = self.D_S(fake_x)  # 11552长度向量
        real_output = self.D_S(x)  # 11552长度向量

        gp = self.calc_gradient_penalty(self.D_S, x.data, fake_x.data)

        LSadv = self.lambda_sadv * (fake_output.mean() - real_output.mean() + self.lambda_gp * gp)
        self.trainerD_S.zero_grad()
        LSadv.backward()
        self.trainerD_S.step()
        return (real_output.mean() - fake_output.mean()).data.mean() * self.lambda_sadv

    def update_structure_generator(self, x, xl, l, t=None):
        fake_x = self.G_S(xl, l)  # fake_x ： [32,3,256,256]
        fake_output = self.D_S(fake_x)  # 向量
        LSadv = -fake_output.mean() * self.lambda_sadv
        LSrec = self.loss(fake_x, x) * self.lambda_l1
        LS = LSadv + LSrec
        if t is not None:
            # weight map based on the distance field
            # whose pixel value increases with its distance to the nearest text contour point of t
            Mt = (t[:, 1:2] + t[:, 2:3]) * 0.5 + 1.0
            t_noise = t.clone()
            t_noise[:, 0:1] = gaussian(t_noise[:, 0:1], stddev=0.2)
            fake_t = self.G_S(t_noise, l)
            LSgly = self.loss(fake_t * Mt, t * Mt) * self.lambda_gly
            LS = LS + LSgly
        self.trainerG_S.zero_grad()
        LS.backward()
        self.trainerG_S.step()
        # global id
        # if id % 60 == 0:
        #    viz_img = to_data(torch.cat((x[0], xl[0], fake_x[0]), dim=2))
        #    save_image(viz_img, '../output/structure_result%d.jpg'%id)
        # id += 1
        return LSadv.data.mean(), LSrec.data.mean(), LSgly.data.mean() if t is not None else 0

    def structure_one_pass(self, x, xl, l, t=None):
        # TODO t 是干嘛的？？？
        LDadv = self.update_structure_discriminator(x, xl, l)
        LGadv, Lrec, Lgly = self.update_structure_generator(x, xl, l, t)
        return [LDadv, LGadv, Lrec, Lgly]

    def update_texture_discriminator(self, x, y):
        # texture transfer: x 风格距离图  [bs, 3, 256, 256]
        # texture transfer: y 风格图  [bs, 3, 256, 256]
        with torch.no_grad():
            fake_y = self.G_T(x)  # 从风格距离图中生成风格图，就像pix2pix那样！！！
            fake_concat = torch.cat((x, fake_y), dim=1)

        fake_output = self.D_T(fake_concat)
        real_concat = torch.cat((x, y), dim=1)
        real_output = self.D_T(real_concat)

        gp = self.calc_gradient_penalty(self.D_T, real_concat.data, fake_concat.data)

        LTadv = self.lambda_tadv * (fake_output.mean() - real_output.mean() + self.lambda_gp * gp)

        self.trainerD_T.zero_grad()
        LTadv.backward()
        self.trainerD_T.step()
        return (real_output.mean() - fake_output.mean()).data.mean() * self.lambda_tadv

    def update_texture_generator(self, x, y, t=None, l=None, VGGfeatures=None, style_targets=None):
        fake_y = self.G_T(x)

        # 计算L_distance
        # 风格距离图变为黑白图
        BW = x[:, 0, :, :].clone().detach().unsqueeze(dim=1)
        # print(BW.shape)
        BW = BW.expand(BW.shape[0], 3, BW.shape[2], BW.shape[3])
        C = BW
        D = x
        X = fake_y
        C.require_grad_ = False
        D.require_grad_ = False
        # Ldistance = 1e-6 * torch.sum((C * D - X * D))
        Ldistance = torch.norm(C * D - X * D, 'fro') * 0.5 * self.lambda_distance

        fake_concat = torch.cat((x, fake_y), dim=1)
        fake_output = self.D_T(fake_concat)
        LTadv = -fake_output.mean() * self.lambda_tadv
        Lrec = self.loss(fake_y, y) * self.lambda_l1
        LT = LTadv + Lrec + Ldistance
        if t is not None:
            with torch.no_grad():
                t[:, 0:1] = gaussian(t[:, 0:1], stddev=0.2)
                source_mask = self.G_S(t, l).detach()
                source = source_mask.clone()
                source[:, 0:1] = gaussian(source[:, 0:1], stddev=0.2)
                smaps_fore = [(A.detach() + 1) * 0.5 for A in self.getmask(source_mask[:, 0:1])]
                smaps_back = [1 - A for A in smaps_fore]
            fake_t = self.G_T(source)
            out = VGGfeatures(fake_t)
            style_losses1 = [self.style_weights[a] * self.gramloss(A * smaps_fore[a], style_targets[0][a]) for a, A in
                             enumerate(out)]
            style_losses2 = [self.style_weights[a] * self.gramloss(A * smaps_back[a], style_targets[1][a]) for a, A in
                             enumerate(out)]
            Lsty = (sum(style_losses1) + sum(style_losses2)) * self.lambda_sty
            LT = LT + Lsty
        # global id
        # if id % 20 == 0:
        #    viz_img = to_data(torch.cat((x[0], y[0], fake_y[0]), dim=2))
        #    save_image(viz_img, '../output/texturee_result%d.jpg'%id)
        # id += 1
        self.trainerG_T.zero_grad()
        LT.backward()
        self.trainerG_T.step()
        return Ldistance.data.mean(), LTadv.data.mean(), Lrec.data.mean(), Lsty.data.mean() if t is not None else 0

    def texture_one_pass(self, x, y, t=None, l=None, VGGfeatures=None, style_targets=None):
        LDadv = self.update_texture_discriminator(x, y)
        Ldiatance, LGadv, Lrec, Lsty = self.update_texture_generator(x, y, t, l, VGGfeatures, style_targets)
        return [Ldiatance, LDadv, LGadv, Lrec, Lsty]

    def save_structure_model(self, filepath, filename):
        torch.save(self.G_S.state_dict(), os.path.join(filepath, filename + '-GS.ckpt'))
        torch.save(self.D_S.state_dict(), os.path.join(filepath, filename + '-DS.ckpt'))

    def save_texture_model(self, filepath, filename):
        torch.save(self.G_T.state_dict(), os.path.join(filepath, filename + '-GT.ckpt'))
        torch.save(self.D_T.state_dict(), os.path.join(filepath, filename + '-DT.ckpt'))
