import torch
import torch.nn.functional as F
import torch.nn
from torch.nn import Module

WEIGHTS_INIT_STDEV = .1


def shortcut_interpolation(image, sc, factor):
    """
    快捷插值？？？
    合法的factor范围：[0.0,2.0]
    当factor在[0.0, 1.0]之间时，笔画由(1-factor) * 256 + factor * 512 组成
    当factor在[1.0, 2.0]之间时, 笔画由(2-factor) * 512 + (factor-1) * 768 组成
    这么设计的结果是，当factor在0-2之间增长时，笔画在256-768之间增长
    :param image:
    :param sc:
    :param factor:
    :return:
    """
    if sc[0]:
        if sc[1]:
            alpha = torch.tensor(max(0.0, 1 - factor))
            beta = 1.0 - torch.sign(factor - 1.0) * (factor - 1.0)
            gamma = torch.tensor(max(0.0, factor - 1.0))
        else:
            alpha = torch.tensor(1.0)
            beta = torch.tensor(0.0)
            gamma = torch.tensor(0.0)
    else:
        alpha = torch.tensor(0.0)
        if sc[1]:
            beta = torch.tensor(1.0)
            gamma = torch.tensor(0.0)
        else:
            beta = torch.tensor(0.0)
            gamma = torch.tensor(1.0)
        pass
    conv1 = _conv_layer(image, 16, 3, 1)
    conv2 = _conv_layer(conv1, 32, 3, 2)
    conv3 = _conv_layer(conv2, 48, 3, 2)
    resid1 = _residual_block(conv3, 3)
    resid2 = _residual_block(resid1, 3)
    resid3 = _residual_block(resid2, 3)
    resid4 = _residual_block(resid3, 3)
    resid4_1 = _residual_block(resid4, 3)
    resid5 = alpha * resid3 + beta * resid4 + gamma * resid4_1
    conv_t1 = _conv_tranpose_layer(resid5, 32, 3, 2)
    conv_t2 = _conv_tranpose_layer(conv_t1, 16, 3, 2)
    conv_t3 = _conv_layer(conv_t2, 3, 9, 1, relu=False)
    preds = F.tanh(conv_t3) * 150 + 255.0 / 2.0
    return preds

def _instance_norm(net, train=True):
    in_channels = net.shape[1]
    var_chape = [in_channels]
    mu = torch.mean(net, dim=[2, 3], keepdim=True)
    sigma_sq = torch.mean(net, dim=[2, 3], keepdim=True)
    shift = torch.tensor(torch.zeros(var_chape))
    scale = torch.tensor(torch.ones(var_chape))
    epsilon = 1e-3
    normalized = (net - mu) / (sigma_sq + epsilon) ** 0.5
    return scale * normalized + shift
    pass


def _conv_layer(net, num_filters, filter_size, strides, relu=True):
    weights_init = _conv_init_vars(net, num_filters, filter_size)
    strides_shape = [strides, strides]
    net = F.conv2d(net, weights_init, stride=strides_shape, padding=0)
    net = _instance_norm(net)
    if relu:
        net = F.relu(net)
    return net


# 初始化卷积层权重
def _conv_init_vars(net, out_channels, filter_size, transpose=False):
    # TODO net就是shortcut_interpolation的image
    in_channels = net.shape[1]
    # TODO shape待定
    if not transpose:
        weights_shape = [filter_size, out_channels, filter_size, in_channels]
    else:
        weights_shape = [filter_size, in_channels, filter_size, out_channels]
    # TODO torch.normal与TF的truncated_normal不太一样！！！
    # 权重应该requires_grad = True
    # torch.normal(mean, std, size, *, out=None) → Tensor
    weights_init = torch.normal(mean=0.0,
                                std=WEIGHTS_INIT_STDEV,
                                size=weights_shape,
                                dtype=torch.float32,
                                requires_grad=True)
    return weights_init


def _residual_block(net, filter_size=3):
    tmp = _conv_layer(net, 48, filter_size, 1)
    return net + _conv_layer(tmp, 48, filter_size, 1, relu=False)


def _conv_tranpose_layer(net, num_filters, filter_size, strides):
    weights_init = _conv_init_vars(net, num_filters, filter_size, transpose=True)
    batch_size = net.shape[0]
    channels = net.shape[1]

    rows, cols = net.shape[2], net.shape[3]

    new_rows, new_cols = rows * strides, cols * strides
    # TODO 把第三个与第一个调换了
    new_shape = [batch_size, num_filters, new_rows, new_cols]
    strides_shape = [strides, strides]

    net = F.conv_transpose2d(input=net,
                             weight=weights_init,
                             stride=strides_shape,
                             padding=0)
    net = net.view([batch_size, num_filters, new_rows, new_cols])
    return F.relu(net)


# class CCC(Module):
#     def __init__(self):
#         super(CCC, self).__init__()
#         self.conv = _conv_layer
#         self.resid = _residual_block
#         self.conv_t = _conv_tranpose_layer


def gram_matrix(activations):
    batch_size, d, h, w = activations.size()
    tensor = activations.view(batch_size, d, -1)
    gram_m = torch.matmul(tensor, tensor.transpose(1, 2))
    return gram_m
