import torch
import numpy as np
from PIL import Image
from torchvision import transforms, models


def load_image(img_path, max_size=800, shape=None, is_path=True, target_size=None):
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
    print(w, h)
    if w >= h and w > max_size:
        size = (int(max_size * (h / w)), max_size)
    elif h >= w and h > max_size:
        size = (max_size, int(max_size * (w / h)))
    else:
        size = h, w

    if shape is not None:
        size = shape

    size=(512, 512)

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
    # if layers is None:
        # layers = {'0': 'conv1_1',  # torch.Size([1, 64, 320, 320])
        #           '5': 'conv2_1',  # torch.Size([1, 128, 160, 160])
        #           '10': 'conv3_1',  # torch.Size([1, 256, 80, 80]
        #           '19': 'conv4_1',  # torch.Size([1, 512，40， 40])
        #           '21': 'conv4_2',  # torch.Size([1, 512, 40, 40]
        #           '28': 'conv5_1'}  # torch.Size([1, 512, 20, 20]

    if layers is None:
        layers = {'3': 'relu1_2',  # torch.Size([1, 64, 320, 320])
                  '8': 'relu2_2',  # torch.Size([1, 128, 160, 160])
                  '17': 'relu3_4',  # torch.Size([1, 256, 80, 80]
                  '26': 'relu4_4',  # torch.Size([1, 512，40， 40])
                  '35': 'relu5_4'}  # torch.Size([1, 512, 20, 20]

    features = {}
    x = image
    # model._modules is a dictionary holding each module in the model
    # features只用到了上面的 6 个层，抽出来分别调用layer()，把图像传入，得到输出。
    for name, layer in model._modules.items():
        x = layer(x)
        if name in layers:
            features[layers[name]] = x

    # print(features.keys())
    # dict_keys(['conv1_1', 'conv2_1', 'conv3_1', 'conv4_1', 'con_2', 'conv5_1'])
    return features


def gram_matrix(tensor):
    """ Calculate the Gram Matrix of a given tensor
        Gram Matrix: https://en.wikipedia.org/wiki/Gramian_matrix
    """
    #     print(tensor.size())
    # get the batch_size, depth, height, and width of the Tensor
    batch, d, h, w = tensor.size()

    # reshape so we're multiplying the features for each channel
    #     tensor = tensor.view(d, h * w)
    tensor = tensor.view(batch, d, h * w)
    #     print(f'tensor size:{tensor.size()}')
    #     print(f'tensor transpose size:{tensor.transpose(1, 2).size()}')
    # calculate the gram matrix
    #     gram = torch.mm(tensor, tensor.t())
    gram = torch.einsum('bij, bjk -> bik', tensor, tensor.transpose(2, 1))
    #     gram = torch.matmul(tensor, tensor.transpose(1, 2))

    return gram