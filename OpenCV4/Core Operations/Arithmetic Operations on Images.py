"""
Goal
Learn several arithmetic operations on images, like addition, subtraction, bitwise operations, and etc.
Learn these functions: cv.add(), cv.addWeighted(), etc.
"""
import numpy as np
import cv2 as cv

img1 = cv.imread('virus.png')
img2 = cv.imread('flag.jpg')
img1 = img1[:210, :355]
"""
图像加法
使用cv.add或者直接+，可以numpy直接图像+图像，可以图像+标量
NOTE OpenCV加法是饱和运算，而Numpy加法是模运算。
"""
# 无符号八位，最大值255
x = np.uint8([250])
y = np.uint8([10])
print(x)  # [250]
print(y)  # [10]
print(cv.add(x, y))  # 250+10 = 260 超过了255就截取255 => 255 [[255]]
print(x + y)  # 250+10 = 260 % 256 = 4 超过255取余数 [4]

add_with_numpy = img1 + img2
add_with_opencv = cv.add(img1, img2)
# cv.imshow('add_with_numpy', add_with_numpy)
# cv.imshow('add_with_opencv', add_with_opencv)
#
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
图像融合blending
这也是图像加法，但是对图像赋予不同的权重，以使其具有融合或透明的感觉。
根据以下等式添加图像：g(x) = (1-alpha)f0(x) + (alpha)f1(x)
alpha取值[0,1]
cv.addWeighted() dst=α⋅img1+β⋅img2+γ
"""

print(img1.shape)
print(img2.shape)
# def addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None)
dst = cv.addWeighted(img1, 1.0, img2, 0.3, 0)
dst2 = cv.addWeighted(img1, 0.7, img2, 0.3, 0)
dst3 = cv.addWeighted(img1, 0.7, img2, 1.0, 0)
dst4 = cv.addWeighted(img1, 1.0, img2, 1.0, 0)
dst5 = cv.addWeighted(img1, 1.0, img2, 0.1, 0)
dst6 = cv.addWeighted(img1, 1.0, img2, 0.1, 0.5)
dst7 = cv.addWeighted(img1, 1.0, img2, 0.1, 0.9)
# cv.imshow('dst', dst)
# cv.imshow('dst2', dst2)
# cv.imshow('dst3', dst3)
# cv.imshow('dst4', dst4)
# cv.imshow('dst5', dst5)
# cv.imshow('dst6', dst6)
# cv.imshow('dst7', dst7)
#
# cv.waitKey(0)
# cv.destroyAllWindows()


"""
按位运算bitwise
这包括按位AND，OR，NOT和XOR操作。
在提取图像的任何部分（如我们将在下一章中看到），
定义和使用非矩形ROI等方面，它们将非常有用。
下面我们将看到一个如何更改图像特定区域的示例。 
"""

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
img1gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
cv.imshow('gray', img1gray)
ret, mask = cv.threshold(img1gray, 50, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)  # 灰度图像，所有像素值取反
cv.imshow('mask', mask)
cv.imshow('mask_inv', mask_inv)
print(type(mask))
print(type(ret))

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2, img2, mask=mask)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
cv.imshow('res', img1)
cv.waitKey(0)
cv.destroyAllWindows()
