import numpy as np
from PIL import Image
import scipy.ndimage as pyimg

# BASE_DIR = '../data/oth'
BASE_DIR = '../data/rawtext/sentence/'

def text_image_preprocessing(filename, t):
    """
    :param filename: 无路径的文件名
    :param t: 0,文本图片，原size；其他，风格图片，宽度2倍拼接，左dis后的风格图片，右原风格图片
    :return: 保存到BASE_DIR下面
    """
    I = np.array(
        Image.open(f'{BASE_DIR}/{filename}')
    )
    BW = I[:, :, 0] > 127
    G_channel = pyimg.distance_transform_edt(BW)
    G_channel[G_channel > 32] = 32
    B_channel = pyimg.distance_transform_edt(1 - BW)
    B_channel[B_channel > 200] = 200
    I[:, :, 1] = G_channel.astype('uint8')
    I[:, :, 2] = B_channel.astype('uint8')
    dot_idx = filename.index('.')
    if t == 0:
        # 文本图片
        Image.fromarray(I).save(f'{BASE_DIR}/{filename[:dot_idx]}_dis.{filename[dot_idx + 1:]}')
        print(f'{BASE_DIR}/{filename[:dot_idx]}_dis.{filename[dot_idx + 1:]} 已保存 ')
    else:
        # 风格图片
        style = np.array(
            Image.open(f'{BASE_DIR}/{filename}')
        )
        res = Image.fromarray(
            np.concatenate((I, style), axis=1)
        )
        res.save(f'{BASE_DIR}/{filename[:dot_idx]}_style.{filename[dot_idx + 1:]}')
        print(f'{BASE_DIR}/{filename[:dot_idx]}_style.{filename[dot_idx + 1:]} 已保存')


text_image_preprocessing('重庆邮电大学生.png', 0)

