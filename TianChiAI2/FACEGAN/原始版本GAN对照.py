#!/usr/bin/env python
# coding: utf-8
import numpy as np
import os

import torchvision.transforms as transforms
from torchvision.utils import save_image
from torch.utils.data import DataLoader
from torchvision import datasets
from torch.autograd import Variable
from torch.optim import Adam

import torch.nn as nn
import torch.nn.functional as F
import torch

# os.makedirs("output", exist_ok=True)

n_epochs = 20
batch_size = 64
lr = 0.001  # adam学习率
b1 = 0.5  # 梯度一阶动量的衰减
b2 = 0.999
n_cpu = 6
sample_interval = 100  # 图像样本之间的间隔
channels = 1
img_size = 28
latent_dim = 100  # 潜在空间的维数

img_shape = (channels, img_size, img_size)

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

os.makedirs("datasets/mnist", exist_ok=True)

# 配置dataloader
transform = transforms.Compose([
    transforms.Resize(img_size),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])
"""
该数据集包含60,000个用于训练的示例和10,000个用于测试的示例。
这些数字已经过尺寸标准化并位于图像中心，
图像是固定大小(28x28像素)，
其值为0到1。
"""
dataset = datasets.MNIST(
    "datasets/mnist",
    train=True,
    download=True,
    transform=transform
)
dataloader = DataLoader(
    dataset,
    batch_size=batch_size,
    shuffle=True
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

for epoch in range(n_epochs):
    for i, (imgs, _) in enumerate(dataloader):
        #         print(f'imgs {imgs.shape}')  # torch.Size([64, 1, 28, 28])

        # 对抗性的 标定好的真实数据
        #         valid = Variable(
        #             Tensor(imgs.size(0), 1).fill_(1.0),
        #             requires_grad=False
        #         )
        #         fake = Variable(
        #             Tensor(imgs.size(0), 1).fill_(0.0),
        #             requires_grad=False
        #         )
        # 新版本的torch不需要Variable了
        # 1
        valid = Tensor(np.ones((imgs.size(0), 1)))
        # 0
        fake = Tensor(np.zeros((imgs.size(0), 1)))

        # 配置输入
        #         real_imgs = Variable(imgs.type(Tensor))
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
        # 噪声采样作为生成器输入
        z = Tensor(np.random.normal(0, 1, (imgs.shape[0], latent_dim)))

        #         print(f'z {z.shape}')  # torch.Size([64, 100])

        # 生成一个 batch 的图像
        gen_imgs = generator(z)
        #         print(f'gen_imgs {gen_imgs.shape}')  # torch.Size([64, 3, 28, 28])

        # loss 度量生成器欺骗判别器的能力，看有多少被判别器判别为fake和valid
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

        print(gen_imgs.shape)

        batches_done = epoch * len(dataloader) + i
        if batches_done % sample_interval == 0:
            print(f'save {batches_done}')
            # 保存前 25 个？
            os.makedirs('outputs/images_lr001_3', exist_ok=True)
            save_image(gen_imgs.data[:25],
                       "outputs/images_lr001_3/%d.png" % batches_done, nrow=5,
                       normalize=True)



