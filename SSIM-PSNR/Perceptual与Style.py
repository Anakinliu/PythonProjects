from utils import *
from numpy import linalg as LA

# NST
target1_img_path = 'data/10000.png'
# ShapeMatchingGAN
target2_img_path = 'data/fire_fire-huo_20.png'
# 风格图像
style_img_path = 'data/fire.png'


layers = {'0': 'relu1_1',
          '6': 'relu2_1',
          '11': 'relu3_1',
          '20': 'relu4_1',
          '29': 'relu5_1'}

# 获取特征部分
vgg = models.vgg19(pretrained=True).features

# 冻结所有参数。
for param in vgg.parameters():
    param.requires_grad_(False)
# move the model to GPU, if available
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = "cpu"

vgg.to(device)

# 加载图片
target1 = load_image(target1_img_path).to(device)
target2 = load_image(target2_img_path).to(device)
style = load_image(style_img_path).to(device)

# 计算内容图在VGG的不同层的特征
target1_features = get_features(target1, vgg)
target2_features = get_features(target2, vgg)
style_features = get_features(style, vgg)

target1_features_lst = []
for v in target1_features.values():
    batch, d, h, w = v.size()
    target1_features_lst.append(v.view(-1, h*w).clone().detach().numpy())

target2_features_lst = []
for v in target2_features.values():
    batch, d, h, w = v.size()
    target2_features_lst.append(v.view(-1, h*w).clone().detach().numpy())

style_features_lst = []
for v in style_features.values():
    batch, d, h, w = v.size()
    style_features_lst.append(v.view(-1, h*w).clone().detach().numpy())

# 由风格特征计算Gram矩阵
# target1_grams = {layer: gram_matrix(target1_features[layer]) for layer in target1_features}
# target2_grams = {layer: gram_matrix(target2_features[layer]) for layer in target2_features}
# style_grams = {layer: gram_matrix(style_features[layer]) for layer in style_features}

# Perceptual
sum1 = 0
sum2 = 0
for i in range(5):
    # print(target1_features_lst[i])
    # print(target2_features_lst[i])
    sum1 += LA.norm(target1_features_lst[i] - style_features_lst[i], 2) ** 2 / 320 / 320
    sum2 += LA.norm(target2_features_lst[i] - style_features_lst[i], 2) ** 2 / 320 / 320
    # sum1 += np.mean((target1_features_lst[i] - style_features_lst[i]) ** 2) ** 2 / 320 / 320
    # sum2 += LA.norm(target2_features_lst[i] - style_features_lst[i], 2) ** 2 / 320 / 320
print('Perceptual')
print(f'NST: {sum1}')
print(f'ShapeMatchingGAN:{sum2}')
# print(target1_grams.keys())
# LA.norm()

# Style loss
sum1 = 0
sum2 = 0
for i in range(5):
    # print(target1_features_lst[i])
    # print(target2_features_lst[i])
    sum1 += LA.norm(target1_features_lst[i].dot(target1_features_lst[i].T) - style_features_lst[i].dot(style_features_lst[i].T), 2) ** 2 / 320 / 320
    sum2 += LA.norm(target2_features_lst[i].dot(target2_features_lst[i].T) - style_features_lst[i].dot(style_features_lst[i].T), 2) ** 2 / 320 / 320
print('Style')
print(f'NST: {sum1}')
print(f'ShapeMatchingGAN:{sum2}')
