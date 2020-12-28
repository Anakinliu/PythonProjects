import matplotlib.pyplot as plt
from utils import *
from imodels import Image_Transform_Net
import torch.optim as optim
import datetime
import os
import numpy as np
content_img_path = '../content/cqupt.jpg'
style_img_path = '../style/lotus.jpg'
date = datetime.datetime.now()
target_img_path = f'../output/{date.month}-{date.day}-{date.hour}-{date.minute}-{date.second}'
os.makedirs(target_img_path)
state_path = '../save/save'

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

vgg = models.vgg19(pretrained=True).features
# 冻结VGG所有参数。
for param in vgg.parameters():
    param.requires_grad_(False)

vgg.to(device)
# 加载图片
content = load_image(content_img_path).to(device)
# 样式图片被缩放以易于编码，并强制样式图像与内容图像的大小相同。
style = load_image(style_img_path, shape=content.shape[-2:]).to(device)

content_features = get_features(normalize_image_for_pre_vgg(content), vgg)
print(content_features)

# image_transform_net = Image_Transform_Net()
# image_transform_net.to(device)
#
# res = image_transform_net(style)
# print(res.shape)  # torch.Size([1, 3, 512, 512])
# img_data = im_convert2(res)
# print(img_data.shape)  # torch.Size([1, 3, 512, 512])
#
# # print(img.dtype)
#
# Image.fromarray((255 * img_data).astype('uint8')).save(f'{target_img_path}/res.png')

