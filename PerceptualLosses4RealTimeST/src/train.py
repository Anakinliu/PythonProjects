import matplotlib.pyplot as plt
from utils import *
from imodels import Image_Transform_Net
import torch.optim as optim
import datetime
import os
import numpy as np
content_img_path = '../content/cqupt.jpg'
style_img_path = '../style/delaunay.jpg'
date = datetime.datetime.now()
target_img_path = f'../output/{date.month}-{date.day}-{date.hour}-{date.minute}-{date.second}'
os.makedirs(target_img_path)
state_path = '../save/save'

style_weights = {'relu1_2': 1.,
                 'relu2_2': .75,
                 'relu3_4': .2,
                 'relu4_4': .2,
                 'relu5_4': .2
                 }
# 3, 8, 17, 26, 35
content_weight = 1  # alpha
style_weight = 1e3  # beta
TV_WEIGHT = 1e-7
steps = 5000  # decide how many iterations to update your image (5000)
show_every = 100

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

vgg = models.vgg19(pretrained=True).features
# 冻结VGG所有参数。
for param in vgg.parameters():
    param.requires_grad_(False)

vgg.to(device)

image_transform_net = Image_Transform_Net()
image_transform_net.to(device)

# 加载图片
content = load_image(content_img_path).to(device)
# 样式图片被缩放以易于编码，并强制样式图像与内容图像的大小相同。
style = load_image(style_img_path, shape=content.shape[-2:]).to(device)

# 计算内容图在VGG的不同层的特征
content_features = get_features(content, vgg)
# 计算风格图在VGG的不同层的特征
style_features = get_features(style, vgg)

# 由风格特征计算Gram矩阵
style_grams = {layer: gram_matrix(style_features[layer]) for layer in style_features}

# target = torch.rand(content.shape, requires_grad=True, device='cuda')
x = content.clone().requires_grad_(True).to(device)

# 先经过Image Transform Net


def train():

    optimizer = optim.Adam(image_transform_net.parameters(), lr=0.003)
    image_transform_net.train()
    for ii in range(1, steps + 1):

        y_hat = image_transform_net(x)
        target_feature_s = get_features(y_hat, vgg)
        # print(np.prod(tuple(content_features['relu4_4'].shape[-3:])))
        # print(tuple(content_features['relu4_4'].shape[-3:]))
        # content_loss = ((target_feature_s['relu4_4'] - content_features['relu4_4']) ** 2)
        l1 = np.prod(tuple(content_features['relu2_2'].shape[-3:]))
        content_loss = torch.dist(target_feature_s['relu2_2'], content_features['relu2_2'], p=2) ** 2 / l1

        style_loss = 0
        for layer in style_weights:
            target_feature = target_feature_s[layer]
            target_gram = gram_matrix(target_feature)
            _, d, h, w = target_feature.shape
            style_gram = style_grams[layer]
            layer_style_loss = style_weights[layer] * torch.mean((target_gram - style_gram) ** 2)
            style_loss += layer_style_loss / (d * h * w)

        # calculate total variation regularization (anisotropic version)
        # https://www.wikiwand.com/en/Total_variation_denoising
        diff_i = torch.sum(torch.abs(y_hat[:, :, :, 1:] - y_hat[:, :, :, :-1]))
        diff_j = torch.sum(torch.abs(y_hat[:, :, 1:, :] - y_hat[:, :, :-1, :]))
        tv_loss = TV_WEIGHT * (diff_i + diff_j)

        total_loss = content_weight * content_loss + style_weight * style_loss + tv_loss
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()

        if ii % show_every == 0:
            print(f'{ii}: Total loss: {total_loss.item()}')
            # TODO 213
            img_data_to_save = im_convert(y_hat)
            # print(img.dtype)
            Image.fromarray((255 * img_data_to_save).astype('uint8')).save(f'{target_img_path}/{ii}.png')

    torch.save(image_transform_net.state_dict(), state_path)
    print('model saved')
    # 加载
    # model = TheModelClass(*args, **kwargs)
    # model.load_state_dict(torch.load(PATH))
    # model.eval()

train()

