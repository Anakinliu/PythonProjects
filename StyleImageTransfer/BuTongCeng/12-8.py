from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np

import torch
import torch.optim as optim
from torchvision import transforms, models

from utils import *
import os

content_img_path = 'content/Ea.png'
style_img_path = 'style/fire.png'
# target_img_path = 'target/output'
target_img_path = 'target/12-8/dis_E_fire+c_w-1e-3+conv5_1-05+conv4_1-05+conv3_1-05/'
if not os.path.exists(target_img_path):
    os.makedirs(target_img_path)

style_weights = {'conv1_1': 1.,
                 'conv2_1': 0.75,
                 'conv3_1': 0.5,
                 'conv4_1': 0.5,
                 'conv5_1': 0.5
                 }

content_weight = 1e-3  # alpha
style_weight = 1e3  # beta

steps = 10000  # decide how many iterations to update your image (5000)

# 获取特征部分
vgg = models.vgg19(pretrained=True).features

# 冻结所有参数。
for param in vgg.parameters():
    param.requires_grad_(False)
# move the model to GPU, if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

vgg.to(device)

# 加载图片
content = load_image(content_img_path).to(device)
# 样式图片被缩放以易于编码，并强制样式图像与内容图像的大小相同。
style = load_image(style_img_path, shape=content.shape[-2:]).to(device)

# display the images
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
# content and style ims side-by-side
ax1.imshow(im_convert(content))
ax2.imshow(im_convert(style))

plt.show()

# 计算内容图在VGG的不同层的特征
content_features = get_features(content, vgg)
# 计算风格图在VGG的不同层的特征
style_features = get_features(style, vgg)

# 由风格特征计算Gram矩阵
style_grams = {layer: gram_matrix(style_features[layer]) for layer in style_features}

# 直接从内容图像构造目标图像
target = content.clone().requires_grad_(True).to(device)
# target = torch.rand(size=content.shape, device='cuda').requires_grad_(True)
print(target.is_leaf)

def train():
    # for displaying the target image, intermittently
    show_every = 50

    # iteration hyperparameters
    # optimizer = optim.Adam([target], lr=0.003)
    optimizer = optim.Adam([target], lr=0.03)

    for ii in range(1, steps + 1):

        # 每一次迭代，target图像都会被更新，需要重新计算target的特征表示
        target_feature_s = get_features(target, vgg)

        # 每一次迭代，计算content loss， 因为target_features在变，虽然content_features没变
        content_loss = torch.mean((target_feature_s['conv4_2'] - content_features['conv4_2']) ** 2)

        # 计算 style loss
        # initialize the style loss to 0
        style_loss = 0
        # then add to it for each layer's gram matrix loss
        # 每此循环计算的是L_style^l
        for layer in style_weights:  # 得到的是key，网络层的name
            # get the "target" style representation for the layer
            # 从layer层里得到target 的样式表示
            target_feature = target_feature_s[layer]
            # 从 target 的样式表示得到 gram 矩阵
            target_gram = gram_matrix(target_feature)
            _, d, h, w = target_feature.shape
            # get the "style" style representation
            # 得到layer层的样式gram
            style_gram = style_grams[layer]
            # the style loss for one layer, weighted appropriately
            layer_style_loss = style_weights[layer] * torch.mean((target_gram - style_gram) ** 2)
            # add to the style loss
            # 按照论文里的来
            style_loss += layer_style_loss / (d * h * w)

        # 计算总的 loss
        total_loss = content_weight * content_loss + style_weight * style_loss

        # update your target image
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()

        # display intermediate images and print the loss
        if ii % show_every == 0:
            print(f'{ii}: Total loss: {total_loss.item()}')
            plt.imshow(im_convert(target))
            # plt.show()
            plt.savefig(f'{target_img_path}/{ii}.png', dpi=200, format='png')

train()