from PIL import ImageFont, ImageDraw, Image
import numpy as np
"""
目前只考虑了写一行。。。
"""
target_dir = '../data/rawtext/sentence/'
user_input = input("输入文字\n")
print(f'输入了：{user_input}')
user_len = len(user_input)
left_padding = 40
up_padding = 20
single_text_w = 260
single_text_h = 320
# 注意这里一定要是彩色图片
# image = cv2.imread('pil_text.png')
# 定义宋体路径
image = Image.new(mode='RGB', size=(left_padding + single_text_w * user_len, single_text_h), color=0)
fontpath = r'G:\字体\H063-01中文字体\华文新魏.TTF'
# 创建字体对象，并且指定字体大小
font = ImageFont.truetype(fontpath, single_text_w-10)
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
