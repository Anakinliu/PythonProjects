#!/usr/bin/env python
# coding: utf-8
import numpy as np
import os
import torch.nn as nn
import torch.nn.functional as F
import torch
import torchvision.transforms as transforms
from torchvision.utils import save_image
from torch.optim import Adam
from torch.utils.data import DataLoader
from PIL import Image

from FACEGAN.TWDNE数据集 import TWDNE
import matplotlib.pyplot as plt
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H-%M-%S")

# helper function to un-normalize and display an image
def show_image(img):
    img = img / 2 + 0.5  # unnormalize
    plt.imshow(np.transpose(img, (1, 2, 0)))  # convert from Tensor image
    plt.show()

n_epochs = 20  # 20 epoch
batch_size = 8

lr = 0.001  # adam学习率
b1 = 0.5  # 梯度一阶动量的衰减
b2 = 0.999

n_cpu = 6  # CPU数量？
sample_interval = 10  # 图像样本之间的间隔
channels = 3  # 输入图像的通道数
img_size = 128  # 图像大小，正方形，和比赛给的大小一样
latent_dim = 128  # 潜在空间的维数
img_shape = (channels, img_size, img_size)  # 输入image的形状
outputs_path = f'{dt_string}-batch{batch_size}-lat_dim{latent_dim}-增加D-channel-FP16'
model_path = f'saves/{outputs_path}/model'
linear_in_feat = 16384
cuda = True


class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()

        # 输入特征，输出特征
        def block(in_feat, out_feat, normalize=True):
            layers = [nn.Linear(in_feat, out_feat)]
            # 这个normalize有啥用
            if normalize:
                layers.append(nn.BatchNorm1d(out_feat, 0.8))
            layers.append(nn.LeakyReLU(0.2, inplace=True))
            return layers

        # 潜在维度，输入的图像形状
        self.model = nn.Sequential(
            *block(latent_dim, 512, normalize=False),
            *block(512, 1024),
            *block(1024, 2048),
            nn.Linear(2048, int(np.prod(img_shape))),
            nn.Tanh()
        )
        pass

    def forward(self, x):
        img = self.model(x)
        # print(img.size(0))  # 64
        img = img.view(img.size(0), *img_shape)
        return img


class Discriminator(nn.Module):

    def __init__(self):
        super(Discriminator, self).__init__()

        def cnn_block(in_channels, out_channels, kernel_size, padding, stride=1, pool_paras=(2, 2, 0)):
            # pool_paras: kernel_size, stride, padding
            layers = [nn.Conv2d(in_channels, out_channels, kernel_size, stride=stride, padding=padding),
                      nn.MaxPool2d(*pool_paras)]
            return layers

        def linear_block(in_feat, out_feat):
            layers = [nn.Linear(in_feat, out_feat),
                      nn.LeakyReLU(0.2, inplace=True),
                      nn.Dropout(0.2)]
            return layers
        self.cnn = nn.Sequential(
            *cnn_block(3, 16, 3, padding=1),
            *cnn_block(16, 32, 3, padding=1),
            *cnn_block(32, 64, 3, padding=1)
        )
        self.linear = nn.Sequential(
            *linear_block(linear_in_feat, 2048),
            *linear_block(2048, 512),
            *linear_block(512, 64),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )
        pass

    def forward(self, img):
        # print(img.shape)  # torch.Size([64, 3, 112, 112])

        # img_flat = img.view(img.size(0), -1)
        # validity = self.model(img_flat)

        # CNN 直接接收图像
        img = self.cnn(img)
        # print(img.shape)  # 注意cnn的输出通道数！torch.Size([128, 32, 8, 8])
        img = img.view(-1, linear_in_feat)
        # 这里是写死的：
        validity = self.linear(img)
        return validity

# 损失函数
# adversarial_loss = torch.nn.BCELoss()
"""
RuntimeError: torch.nn.functional.binary_cross_entropy and torch.nn.BCELoss are unsafe to autocast.
Many models use a sigmoid layer right before the binary cross entropy layer.
In this case, combine the two layers using torch.nn.functional.binary_cross_entropy_with_logits
or torch.nn.BCEWithLogitsLoss.  binary_cross_entropy_with_logits and BCEWithLogits are
safe to autocast.
"""
adversarial_loss = torch.nn.BCEWithLogitsLoss()

# 初始化生成器与判别器
generator = Generator()
discriminator = Discriminator()

if cuda:
    generator.cuda()
    discriminator.cuda()
    adversarial_loss.cuda()

# 配置dataloader
# 数据集图像比imgsize 大
transform = transforms.Compose([
    transforms.Resize(img_size),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
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

# Tensor = torch.FloatTensor
Tensor = torch.cuda.FloatTensor

better_g_loss = float('inf')

# create once at the beginning if training
scaler = torch.cuda.amp.GradScaler()

for epoch in range(n_epochs):
    one_epoch_loss = 0
    for i, imgs in enumerate(dataloader):
        # show_image(imgs[0])
        # break
        # print(f'imgs {imgs.shape}')  # torch.Size([64, 1, 28, 28])
        # print(imgs.shape)
        # 对抗性的 标定好的真实数据

        optimizer_G.zero_grad()

        with torch.cuda.amp.autocast():
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
            # 噪声采样作为生成器输入
            z = Tensor(np.random.normal(0, 1, (imgs.shape[0], latent_dim)))  # 噪声采样作为生成器输入

            # 生成一个 batch 的图像
            gen_imgs = generator(z)
            #         print(f'gen_imgs {gen_imgs.shape}')  # torch.Size([64, 3, 28, 28])

            # loss 度量生成器欺骗判别器的能力，
            # 看有多少被判别器判别为 fake 或 valid
            g_loss = adversarial_loss(discriminator(gen_imgs), valid)

        scaler.scale(g_loss).backward()  # scales the loss AND call backward() to create scaled gradients
        scaler.step(optimizer_G)  # Unscales gradients and calls Or skips optimizer.step()
        scaler.update()

        # g_loss.backward()
        # optimizer_G.step()

        # ---------------------
        #  训练 Discriminator
        # ---------------------

        optimizer_D.zero_grad()

        # 度量判别器对 生成的样本 中的样本进行真实分类的能力
        #         t1 = discriminator(real_imgs)
        #         print(t1.shape)
        #         print(valid.shape)
        #         print(real_imgs.shape)  # torch.Size([64, 1, 28, 28])

        with torch.cuda.amp.autocast():
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

            scaler.scale(d_loss).backward()
            scaler.step(optimizer_D)
            scaler.update()

        # d_loss.backward()
        # optimizer_D.step()

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
            save_image(gen_imgs.data[:36],
                       f'outputs/{outputs_path}/{batches_done}.png', nrow=6,
                       normalize=True)
        pass
    # 保存有进步的epoch的模型，后面的更好的会覆盖前面的
    one_epoch_loss /= len(dataloader)
    if one_epoch_loss < better_g_loss:
        better_g_loss = one_epoch_loss
        # 保存 G
        os.makedirs(model_path, exist_ok=True)
        torch.save(generator.state_dict(), f'{model_path}.pt')
