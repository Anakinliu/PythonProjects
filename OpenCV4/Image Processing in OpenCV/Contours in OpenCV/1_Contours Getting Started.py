"""
https://docs.opencv.org/master/d4/d73/tutorial_py_contours_begin.html
"""
"""
目标
了解轮廓是什么。
学习查找轮廓，绘制轮廓等。您将看到以下功能：cv.findContours（），cv.drawContours（）

什么是轮廓？
轮廓可以简单地解释为: 
连接具有相同颜色或强度的所有连续点（沿边界）的曲线。
轮廓是用于形状分析以及对象检测和识别的有用工具。

为了获得更高的准确性，请使用二进制图像。
因此，在找到轮廓之前，请应用阈值或canny边缘检测(threshold or canny edge detection)。
从OpenCV 3.2开始，findContours（）不再修改源图像。
在OpenCV中，找到轮廓就像从黑色背景中找到白色物体。
因此请记住，要找到的对象应该是白色，背景应该是黑色。

"""

import numpy as np
import cv2 as cv
im = cv.imread('../dog.png')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)

# 第一个是源图像，第二个是轮廓检索模式，第三个是轮廓逼近方法。
# contours轮廓是图像中所有轮廓的Python列表。
# 每个单独的contours轮廓都是对象边界点的（x，y）坐标的Numpy数组。
res, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(type(res))
# print(type(contours))
# print(type(hierarchy))
# print(res.shape)
# print(hierarchy.shape)
print(contours)
cv.imshow('gray', imgray)
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()
