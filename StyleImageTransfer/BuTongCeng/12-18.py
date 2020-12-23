from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
import torch
import torch.optim as optim
# from torchvision import transforms, models

from utils import *
import os

content_img_path = 'content/一_dis.png'
style_img_path = 'style/lotus.jpg'
# target_img_path = 'target/output'
# target_img_path = 'target/12-18/0LSgly0+lotus+一+content_init+content3_1+c_w-1e-3+conv5_1-05+conv4_1-05+conv3_1-05/'
# if not os.path.exists(target_img_path):
#     os.makedirs(target_img_path)

style_weights = {'conv1_1': 0.1,
                 'conv2_1': 0.2,
                 'conv3_1': 0.3,
                 'conv4_1': 0.5,
                 'conv5_1': 1.
                 }

# content_weight = 1e-3  # alpha
content_weight = 0  # alpha
style_weight = 1e3  # beta
LsGly_weight = 1e3


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


