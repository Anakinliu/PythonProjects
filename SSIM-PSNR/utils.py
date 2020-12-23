import torch
import numpy as np
from PIL import Image
from torchvision import transforms, models


def load_image(img_path, shape=None, is_path=True, target_size=None):
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
        image = Image.new(mode="RGB", size=target_size)
    # PIL的Image的是长，宽
    # print(image.size)
    # print(type(image))
    # large images will slow down processing
    w, h = image.size

    if shape is not None:
        size = shape

    size = h, w

    # transforms的size是 h, w
    in_transform = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406),
                             (0.229, 0.224, 0.225))])

    # discard the transparent, alpha channel (that's the :3) and add the batch dimension
    # unsqueeze(0)  在第 0 维度设为了 1
    image = in_transform(image)[:3, :, :].unsqueeze(0)
    print(image.shape)
    return image


# helper function for un-normalizing an image
# and converting it from a Tensor image to a NumPy image for display
def im_convert(tensor):
    """ Display a tensor as an image. """

    image = tensor.to("cpu").clone().detach()
    image = image.numpy().squeeze()  # 消除长度为1的维度
    image = image.transpose(1, 2, 0)
    image = image * np.array((0.229, 0.224, 0.225)) + np.array((0.485, 0.456, 0.406))
    image = image.clip(0, 1)

    return image


def get_features(image, model, layers=None):
    """ Run an image forward through a model and get the features for
        a set of layers. Default layers are for VGGNet matching Gatys et al (2016)
    """

    ## TODO: Complete mapping layer names of PyTorch's VGGNet to names from the paper
    ## Need the layers for the content and style representations of an image
    # 以 320x320图片为例
    if layers is None:
        layers = {'0': 'relu1_1',
                  '6': 'relu2_1',
                  '11': 'relu3_1',
                  '20': 'relu4_1',
                  '29': 'relu5_1'}

    features = {}
    x = image
    # model._modules is a dictionary holding each module in the model
    # features只用到了上面的 6 个层，抽出来分别调用layer()，把图像传入，得到输出。
    for name, layer in model._modules.items():
        # print(name)
        x = layer(x)
        if name in layers:
            features[layers[name]] = x
            # print(x)

    # print(features.keys())
    # dict_keys(['conv1_1', 'conv2_1', 'conv3_1', 'conv4_1', 'conv4_2', 'conv5_1'])
    return features
