"""
Goal
Learn to:

Access pixel values and modify them 得到，修改像素值
Access image properties 得到img属性
Set a Region of Interest (ROI) 设置ROI
Split and merge images 分割，合并图像

大部分与Numpy而不是OPenCV相关
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# -------------
"""
# Accessing and Modifying pixel values
"""
img = cv.imread('virus.png')

px = img[50, 50]
print(px)

# accessing only blue pixel
# blue = img[100, 100, 0]  # 通道0就是b， 1是， 2是r,BGR
blue = img.item(100, 100, 0)  # 使用numpy方法更快
print(blue)

# modify the pixel values the same way.
img.itemset((100, 100, 0), 255)  # 修改一点的像素值

# cv.imshow('corona', img)
# cv.waitKey(0)
# cv.destroyAllWindows()


# -------------
"""
# Accessing Image Properties
 include number of rows, columns, 
 and channels; type of image data; number of pixels; etc.
"""
# shape of image
print(img.shape)  # rows, columns, and channels
# 如果是灰度图像，没有最后的channels
height, width, _ = img.shape

# Total number of pixels is accessed by img.size:
print(img.size)  # 就是shape各项乘积

# Image datatype
print(img.dtype)  # debug注意，很多错误都是由于invalid datatype.

"""
图像识别时，有时不需要真个图像作为输入，你需要的只是ROI
"""
red_ball = img[height // 2 - 30: height // 2 + 10, width // 2 - 10:width // 2 + 30]
img[:40, :40] = red_ball  # 贴上一块

# cv.imshow('corona', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
分离，合并颜色通道
"""

# 直接使用数组操作分割
b_ = img[:, :, 0]
# 借助numpy，设置所有红色像素为0
no_red = img[:, :, 2] = 0

b, g, r = cv.split(img)  # split操作比较耗时！！！
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
mer = cv.merge((b, g, r))

# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)
# cv.imshow('merge', mer)
# cv.imshow('gray', gray)

# cv.imshow('no red', no_red)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
Making Borders for Images (Padding)
"""
BLUE = [255,0,0]
img1 = cv.imread('virus.png')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()