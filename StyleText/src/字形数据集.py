from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os
import scipy.ndimage as pyimg
from skimage import morphology

# FLAG = 1
#
# if FLAG:
#     target_dir = '../data/oth/words/raw/'
#     user_input = input("输入一个文字\n")
# else:
#     target_dir = '../data/oth/sentence/raw/'
#     user_input = input("输入若干文字\n")
RAW_DIR = '../data/oth/glyph/yaheiB_raw/'
DIS_DIR = '../data/oth/glyph/yaheiB_dis/'
SKEL_DIR = '../data/oth/glyph/yaheiB_skel/'

with open('../data/常用1000个文字.txt', 'r', encoding='utf-8') as f:
    user_input = f.readline()

# print(f'你输入了：{user_input}')

user_len = len(user_input)

left_padding = 60
up_padding = 20
single_text_w = 320
single_text_h = 320
# 注意这里一定要是彩色图片
# image = cv2.imread('pil_text.png')
# 定义宋体路径
fontpath = r'G:\字体\yaheiB.TTF'

def raw_text():
    for i in range(user_len):
        image = Image.new(mode='RGB',
                          size=(single_text_w, single_text_h),
                          color=0)
        font = ImageFont.truetype(fontpath, single_text_w - 90)
        img_pil = image
        draw = ImageDraw.Draw(img_pil)
        # 在图像上写上你要写的子
        draw.text((left_padding, up_padding), user_input[i], font=font, fill=(255, 255, 255))
        # 把PIL的image格式转换回成array格式
        save_image = np.array(img_pil)
        save_path = '%s%04d.png' % (RAW_DIR, i)
        Image.fromarray(save_image).save(save_path)
        print(f'{save_path} 已保存')





def dis_text():

    file_names = os.listdir(RAW_DIR)
    for file in file_names:
        # p = 'f'{raw_dir}{file}'
        I = np.array(
            Image.open(f'{RAW_DIR}{file}')
        )
        # RGB
        BW = I[:, :, 0] > 127

        G_channel = pyimg.distance_transform_edt(BW)
        G_channel[G_channel > 32] = 32
        B_channel = pyimg.distance_transform_edt(1 - BW)
        B_channel[B_channel > 200] = 200
        I[:, :, 1] = G_channel.astype('uint8')
        I[:, :, 2] = B_channel.astype('uint8')
        save_path = '%s%s.png' % (DIS_DIR, file[:4])
        Image.fromarray(I).save(save_path)
        print(save_path)


# 此方法废弃
# def skel_text():
#     file_names = os.listdir(RAW_DIR)
#     for file in file_names:
#         I = np.array(
#             Image.open(f'{RAW_DIR}{file}').convert('L').convert('1')
#         )
#         skel = morphology.skeletonize(I)
#         save_path = '%s%s.png' % (SKEL_DIR, file[:4])
#         Image.fromarray(skel).save(save_path)
#         print(save_path)


raw_text()
# dis_text()
# skel_text()