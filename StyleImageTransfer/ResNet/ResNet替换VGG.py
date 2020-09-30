from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

import torch
import torch.optim as optim
import requests
from torchvision import transforms, models


# ### 预训练模型Resnet152
res = models.resnet152(pretrained=True)

# for param in res.parameters():
#     param.requires_grad_(False)

device = torch.device("cuda")


def load_image(img_path, max_size=400, shape=None, is_path=True, target_size=None):
    ''' Load in and transform an image, making sure the image
       is <= 400 pixels in the x-y dims.'''
#     if "http" in img_path:
#         response = requests.get(img_path)
#         image = Image.open(BytesIO(response.content)).convert('RGB')
#     else:
#         image = Image.open(img_path).convert('RGB')
    
    if is_path:
        image = Image.open(img_path).convert('RGB')
    else:  # 随机生成图片
        image = Image.new(mode = "RGB", size = target_size)
#     print(image.size)
#     print(type(image))
    # large images will slow down processing
    if max(image.size) > max_size:
        # 截取图片大小
        size = max_size
    else:
        size = max(image.size)
    
    if shape is not None:
        size = shape
        
    in_transform = transforms.Compose([
                        transforms.Resize(size),
                        transforms.ToTensor(),
                        transforms.Normalize((0.485, 0.456, 0.406), 
                                             (0.229, 0.224, 0.225))])

    # discard the transparent, alpha channel (that's the :3) and add the batch dimension
    # unsqueeze(0)  在第 0 维度设为了 1
    image = in_transform(image)[:3,:,:].unsqueeze(0)  
    print(image.shape)
    return image


# 按文件名加载图像，并强制样式图像与内容图像的大小相同。
# 加载图片
content = load_image('images/cqupt.jpg').to(device)
# 样式图片被缩放以易于编码
style = load_image('images/delaunay.jpg', shape=content.shape[-2:]).to(device)


# un-normalizing image,并从tensor转为numpy以显示
def im_convert(tensor):
    """ Display a tensor as an image. """
    
    image = tensor.to("cpu").clone().detach()  # clone后，得到tensor包含的data部分
    image = image.numpy().squeeze()  # 消除长度为1的维度
    image = image.transpose(1,2,0)
    image = image * np.array((0.229, 0.224, 0.225)) + np.array((0.485, 0.456, 0.406))
    image = image.clip(0, 1)

    return image


# display the images
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
# content and style ims side-by-side
ax1.imshow(im_convert(content))
ax2.imshow(im_convert(style))


# ### 内容特征，样式特征

# In[24]:


for name, layer in res._modules.items():
    print(name)


# 注意，最后一层，即fc，貌似是分类器，这里要跳过这一层，用不到。

# In[33]:


def get_features(image, model, layers=None):
    """
    让图片前向通过resnet，通过一系列层得到特征，
    """
    if layers is None:
        layers = {
            'layer1':'Bottlenecks_1',
            'layer2':'Bottlenecks_2',
            'layer3':'Bottlenecks_3',
            'layer4':'Bottlenecks_4'
        }
    features = {}
    x = image
    for name, layer in model._modules.items():
        if name == 'fc':
            continue
            
        x = layer(x)
        if name in layers:
            features[layers[name]] = x
    return features


# ### 计算Gram矩阵

# In[28]:


def gram_matrix(tensor):
    """ 计算给定tensor的gram矩阵
        Gram Matrix: https://en.wikipedia.org/wiki/Gramian_matrix
    """
    # get the batch_size, depth, height, and width of the Tensor
    batch, d, h, w = tensor.size()
    
    # reshape so we're multiplying the features for each channel
#     tensor = tensor.view(d, h * w)
    tensor = tensor.view(batch, d, h * w)
#     print(f'tensor size:{tensor.size()}')
#     print(f'tensor transpose size:{tensor.transpose(1, 2).size()}')
    gram = torch.einsum('bij, bjk -> bik', tensor, tensor.transpose(2, 1))
    
    return gram 


# ## 组装

# 我们已经编写了用于提取特征，计算gram矩阵的函数；
# 
# 让我们将所有这些片段放在一起！
# 
# 我们将从图像中提取特征

# #### 提取内容特征，样式特征

# In[34]:


content_features = get_features(content, res)


# In[35]:


style_features = get_features(style, res)


# #### 计算提取的4层layer的Gram矩阵

# In[36]:


style_grams = {layer: gram_matrix(style_features[layer]) for layer in style_features}


# #### 初始化样式迁移的target图像

# In[37]:


target = content.clone().requires_grad_(True).to(device)


# #### 样式表示的3个层的权重，剩的那一个是内容表示

# In[45]:


style_weights = {'Bottlenecks_1': 1.,
                 'Bottlenecks_2': 0.75,
                 'Bottlenecks_3': 0.2}
content_weight = 1
style_weight = 1e3


# In[46]:


target_features = get_features(target, res)


# In[52]:


type(target_features)


# In[51]:


for name in target_features:
    print(name)


# #### 更新target

# In[55]:


show_every = 50

optimizer = optim.Adam([target], lr = 0.03)
steps = 200

for ii in range(1, steps+1):
    
    target_features = get_features(target, res)
    
    content_loss = torch.mean((target_features['Bottlenecks_3'] - content_features['Bottlenecks_3'])**2)
    
    style_loss = 0
    for layer in style_weights:  # layer1,2,4
        # 计算target图像在这一层的gram矩阵
        target_feature = target_features[layer]
        target_gram = gram_matrix(target_feature)
        _, d, h, w = target_feature.shape
        # 取出样式图像style的在这一层的gram
        style_gram = style_grams[layer]
        # 这一层的样式损失
        layer_style_loss = style_weights[layer] * torch.mean((target_gram - style_gram)**2)
        # layer1,2,4层的损失
        style_loss += layer_style_loss / (d * h * w)
        pass
    total_loss = content_weight * content_loss + style_weight * style_loss
    
    optimizer.zero_grad()
    total_loss.backward()
    optimizer.step()
    
    if ii % show_every == 0:
        print('Total loss: ', total_loss.item())
        plt.imshow(im_convert(target))
        plt.show()


# In[56]:


# display content and final, target image
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 10))
ax1.imshow(im_convert(content))
ax2.imshow(im_convert(style))
ax3.imshow(im_convert(target))

