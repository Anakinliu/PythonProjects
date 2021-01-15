from PIL import ImageFont, ImageDraw, Image
import numpy as np

"""
目前只考虑了写一行。。。
"""
FLAG = 1

if FLAG:
    target_dir = '../data/oth/words/raw/'
    user_input = input("输入一个文字\n")
else:
    target_dir = '../data/oth/sentence/raw/'
    user_input = input("输入若干文字\n")

print(f'你输入了：{user_input}')
user_len = len(user_input)
left_padding = 50
right_padding = 10
up_padding = 40
bottom_padding = 0
single_text_w = 260
single_text_h = 320
# 注意这里一定要是彩色图片
# image = cv2.imread('pil_text.png')
# 定义宋体路径
image = Image.new(mode='RGB',
                  size=(left_padding + single_text_w * user_len + right_padding, single_text_h + bottom_padding),
                  color=0)
# fontpath = r'G:\字体\H063-01中文字体\华文新魏.TTF'
fontpath = r'G:\字体\H063-01中文字体\华康楷体W5.TTF'
# 创建字体对象，并且指定字体大小
font = ImageFont.truetype(fontpath, single_text_w - 10)
# font = ImageFont.truetype(fontpath, single_text_w + 500)
# 把array格式转换成PIL的image格式
# img_pil = Image.fromarray(image)
img_pil = image
# 创建一个可用来对其进行draw的对象
draw = ImageDraw.Draw(img_pil)
# 在图像上写上你要写的子
draw.text((left_padding, up_padding), user_input, font=font, fill=(255, 255, 255))
# 把PIL的image格式转换回成array格式
save_image = np.array(img_pil)
Image.fromarray(save_image).save(f'{target_dir}{user_input}.png')
print(f'{target_dir}{user_input}.png 已保存')
