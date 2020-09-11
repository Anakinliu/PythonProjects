#!/usr/bin/env python
# coding: utf-8
import numpy as np
import os
import torch.nn as nn
import torch.nn.functional as F
import torch
import torchvision.transforms as transforms
from torchvision.utils import save_image
from torch.utils.data import DataLoader
from torchvision import datasets
from torch.autograd import Variable
from torch.optim import Adam

from FACEGAN.LFW数据集 import LFW
from torch.utils.data import DataLoader
# os.makedirs("output", exist_ok=True)
from FACEGAN.TWDNE数据集 import TWDNE

n_epochs = 20  # 20 epoch
batch_size = 64  # 一次输入迭代的图片个数
lr = 0.001  # adam学习率
b1 = 0.5  # 梯度一阶动量的衰减
b2 = 0.999
n_cpu = 6  # CPU数量？
sample_interval = 10  # 图像样本之间的间隔
channels = 3  # 输入图像的通道数？
img_size = 256  # 图像大小，正方形，和比赛给的大小一样
img_shape = (channels, img_size, img_size)  # 输入image的形状
latent_dim = 100  # 潜在空间的维数
outputs_path = f'FACEGAN-WITH-TWDNE-脸GAN改-batch{batch_size}'
model_path = f'saves/{outputs_path}/model'
linear_in_feat = 7200

cuda = True if torch.cuda.is_available() else False

class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()

        # 输入特征，输出特征
        def block(in_feat, out_feat, normalize=True):
            layers = [nn.Linear(in_feat, out_feat)]
            if normalize:
                layers.append(nn.BatchNorm1d(out_feat, 0.8))
            layers.append(nn.LeakyReLU(0.2, inplace=True))
            return layers

        # 潜在维度，输入的图像形状
        self.model = nn.Sequential(
            *block(latent_dim, 128, normalize=False),
            *block(128, 256),
            *block(256, 512),
            *block(512, 1024),
            nn.Linear(1024, int(np.prod(img_shape))),
            nn.Tanh()
        )
        pass

    def forward(self, z):
        img = self.model(z)
        img = img.view(img.size(0), *img_shape)
        return img

class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        # 输入图像的形状
        self.model = nn.Sequential(
            nn.Linear(int(np.prod(img_shape)), 512),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )
        pass

    def forward(self, img):
        # print(img.shape)
        img_flat = img.view(img.size(0), -1)
        validity = self.model(img_flat)
        return validity

# 损失函数
adversarial_loss = torch.nn.BCELoss()

# 初始化生成器与判别器
generator = Generator()
discriminator = Discriminator()

if cuda:
    generator.cuda()
    discriminator.cuda()
    adversarial_loss.cuda()

# os.makedirs("datasets/mnist", exist_ok=True)

# 配置dataloader
# 数据集图像比imgsize 大
transform = transforms.Compose([
    transforms.CenterCrop(img_size),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

dataset = TWDNE(transform=transform)
dataloader = DataLoader(
    dataset,
    batch_size=batch_size,
    shuffle=True,
)

# 优化器 有两个，生成器与判别器各一个,更新权重的方法
optimizer_G = Adam(
    generator.parameters(),
    lr=lr,
    betas=(b1, b2)
)
optimizer_D = Adam(
    discriminator.parameters(),
    lr=lr,
    betas=(b1, b2)
)

Tensor = torch.cuda.FloatTensor if cuda else torch.FloatTensor

better_g_loss = float('inf')

for epoch in range(n_epochs):
    one_epoch_loss = 0
    for i, imgs in enumerate(dataloader):
        #         print(f'imgs {imgs.shape}')  # torch.Size([64, 1, 28, 28])
        # print(imgs.shape)
        # 对抗性的 标定好的真实数据
        #         valid = Variable(
        #             Tensor(imgs.size(0), 1).fill_(1.0),
        #             requires_grad=False
        #         )
        #         fake = Variable(
        #             Tensor(imgs.size(0), 1).fill_(0.0),
        #             requires_grad=False
        #         )
        with torch.no_grad():
            # 新版本的torch不需要Variable了
            # 1
            valid = Tensor(np.ones((imgs.size(0), 1)))
            # 0
            fake = Tensor(np.zeros((imgs.size(0), 1)))

        # 配置输入
        real_imgs = imgs.type(Tensor)

        # -----------------
        #  训练 Generator
        # -----------------
        optimizer_G.zero_grad()
        # 噪声采样作为生成器输入
        #         z = Variable(
        #             Tensor(
        #                 np.random.normal(
        #                     0,
        #                     1,
        #                     (imgs.shape[0], latent_dim)
        #                 )
        #             )
        #         )

        z = Tensor(np.random.normal(0, 1, (imgs.shape[0], latent_dim)))  # 噪声采样作为生成器输入

        #         print(f'z {z.shape}')  # torch.Size([64, 100])

        # 生成一个 batch 的图像
        gen_imgs = generator(z)
        #         print(f'gen_imgs {gen_imgs.shape}')  # torch.Size([64, 3, 28, 28])

        # loss 度量生成器欺骗判别器的能力，
        # 看有多少被判别器判别为 fake 或 valid
        g_loss = adversarial_loss(discriminator(gen_imgs), valid)

        g_loss.backward()
        optimizer_G.step()

        # ---------------------
        #  训练 Discriminator
        # ---------------------

        optimizer_D.zero_grad()

        # 度量判别器对 生成的样本 中的样本进行真实分类的能力
        #         t1 = discriminator(real_imgs)
        #         print(t1.shape)
        #         print(valid.shape)

        #         print(real_imgs.shape)  # torch.Size([64, 1, 28, 28])

        real_loss = adversarial_loss(
            discriminator(real_imgs),
            valid
        )
        fake_loss = adversarial_loss(
            discriminator(gen_imgs.detach()),
            fake
        )
        # 为什么要相加再除以 2 ？？？
        d_loss = (real_loss + fake_loss) / 2

        d_loss.backward()
        optimizer_D.step()

        print(
            "[Epoch %d/%d] [Batch %d/%d] [D loss: %f] [G loss: %f]"
            % (epoch,
               n_epochs,
               i,
               len(dataloader),
               d_loss.item(),
               g_loss.item())
        )
        # 累加每个batch的生成器的 loss
        one_epoch_loss += g_loss.item()

        batches_done = epoch * len(dataloader) + i
        if batches_done % sample_interval == 0:
            print(f'save {batches_done}')
            # 保存前 25 个？
            os.makedirs(f'outputs/{outputs_path}', exist_ok=True)
            save_image(gen_imgs.data[:5],
                       f'outputs/{outputs_path}/{batches_done}.png', nrow=5,
                       normalize=True)
        pass
    one_epoch_loss /= len(dataloader)
    if one_epoch_loss < better_g_loss:
        better_g_loss = one_epoch_loss
        # 保存 G
        os.makedirs(model_path, exist_ok=True)
        torch.save(generator.state_dict(), f'{model_path}.pt')
