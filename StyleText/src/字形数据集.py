from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os
import scipy.ndimage as pyimg

# FLAG = 1
#
# if FLAG:
#     target_dir = '../data/oth/words/raw/'
#     user_input = input("输入一个文字\n")
# else:
#     target_dir = '../data/oth/sentence/raw/'
#     user_input = input("输入若干文字\n")
raw_dir = '../data/oth/glyph/kaiti_raw/'
dis_dir = '../data/oth/glyph/kaiti_dis/'

with open('../data/常用1000个文字.txt', 'r', encoding='utf-8') as f:
    user_input = f.readline()

# print(f'你输入了：{user_input}')

user_len = len(user_input)

left_padding = 40
up_padding = 40
single_text_w = 320
single_text_h = 320
# 注意这里一定要是彩色图片
# image = cv2.imread('pil_text.png')
# 定义宋体路径
fontpath = r'G:\字体\H063-01中文字体\华康楷体W5.TTF'

def raw_text():
    for i in range(user_len):
        image = Image.new(mode='RGB',
                          size=(single_text_w, single_text_h),
                          color=0)
        font = ImageFont.truetype(fontpath, single_text_w - 80)
        img_pil = image
        draw = ImageDraw.Draw(img_pil)
        # 在图像上写上你要写的子
        draw.text((left_padding, up_padding), user_input[i], font=font, fill=(255, 255, 255))
        # 把PIL的image格式转换回成array格式
        save_image = np.array(img_pil)
        save_path = '%s%04d.png' % (raw_dir, i)
        Image.fromarray(save_image).save(save_path)
        print(f'{save_path} 已保存')





def dis_text():

    file_names = os.listdir(raw_dir)
    for file in file_names:
        # p = 'f'{raw_dir}{file}'
        I = np.array(
            Image.open(f'{raw_dir}{file}')
        )
        # RGB
        BW = I[:, :, 0] > 127

        G_channel = pyimg.distance_transform_edt(BW)
        G_channel[G_channel > 32] = 32
        B_channel = pyimg.distance_transform_edt(1 - BW)
        B_channel[B_channel > 200] = 200
        I[:, :, 1] = G_channel.astype('uint8')
        I[:, :, 2] = B_channel.astype('uint8')
        save_path = '%s%s.png' % (dis_dir, file[:4])
        Image.fromarray(I).save(save_path)
        print(save_path)

# raw_text()
dis_text()