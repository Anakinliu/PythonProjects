from PIL import ImageFont, ImageDraw, Image
import numpy as np

"""
目前只考虑了写一行。。。
"""
FLAG = 1

if FLAG:
    target_dir = 'data/'
    user_input = input("输入一个文字\n")
else:
    target_dir = 'data/'
    user_input = input("输入若干文字\n")

print(f'你输入了：{user_input}')
user_len = len(user_input)
left_padding = 40
right_padding = 0
up_padding = 0
bottom_padding = 0
single_text_w = 320
single_text_h = 320
black = (0, 0, 0)
white = (255, 255, 255)
# 定义宋体路径
image = Image.new(mode='RGB',
                  size=(single_text_w * user_len + right_padding, single_text_h + bottom_padding),
                  color=black)
# fontpath = r'G:\字体\H063-01中文字体\华文新魏.TTF'
# fontpath = r'G:\字体\H063-03中文字体（含预览图）\花火流光\花火流光.ttf'
fontpath = r'G:\字体\yaheib.TTF'
# 创建字体对象，并且指定字体大小
font = ImageFont.truetype(fontpath, single_text_w - 50)
# 把array格式转换成PIL的image格式
# img_pil = Image.fromarray(image)
img_pil = image
# 创建一个可用来对其进行draw的对象
draw = ImageDraw.Draw(img_pil)
# 在图像上写上你要写的子
draw.text((left_padding, up_padding), user_input, font=font, fill=white)
# 把PIL的image格式转换回成array格式
save_image = np.array(img_pil)
Image.fromarray(save_image).save(f'{target_dir}{user_input}.png')
print(f'{target_dir}{user_input}.png 已保存')
