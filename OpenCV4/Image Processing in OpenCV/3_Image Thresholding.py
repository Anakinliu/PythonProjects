"""
目标在本教程中，您将学习简单的阈值，自适应阈值和Otsu的阈值。
您将学习函数cv.threshold和cv.adaptiveThreshold。

"""

"""
简单地手动指定阈值

对于每个像素，应用相同的阈值。
如果像素值小于阈值，则将其设置为0，否则将其设置为最大值。
函数cv.threshold用于应用阈值。
第一个参数是源图像，它应该是灰度图像，灰度图像,灰度图像。
第二个参数是阈值，用于对像素值进行分类。
第三个参数是分配给超过阈值的像素值的最大值。
OpenCV提供了不同类型的阈值，这由函数的第四个参数给出。
通过使用类型cv.THRESH_BINARY完成上述基本阈值设置。
所有简单的阈值类型为：cv.THRESH_BINARY cv.THRESH_BINARY_INV cv.THRESH_TRUNC cv.THRESH_TOZERO cv.THRESH_TOZERO_INV请参见类型的文档以获取区别。
threshold返回两个值，第一个是使用的阈值，第二个输出是阈值图像。
"""
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# img = cv.imread('jb.jpg', 0)
# print(img)  # 纯白255 纯黑0
# src, thresh, maxval, type[, dst]
# ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  # 大于127的设为255，其它为0
# ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)  # 大于127的设为255，其它为0
# ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)  # 小于阈值127的不变，大于阈值的设为阈值
# ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)  # 大于阈值不变，小于的设为0
# ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)  # 小于的不变，大于的设为0
# titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(2, 3, i + 1), plt.imshow(images[i], cmap='gray', vmin=0, vmax=255)
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])  # 不显示坐标刻度
# plt.show()
# cv.imshow('t4', thresh4)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
自适应阈值

在上一节中，我们使用一个全局值作为阈值。
但这可能并非在所有情况下都很好，例如
如果图像在不同区域具有不同的照明条件。
在这种情况下，自适应阈值可以提供帮助。
在此，算法基于像素周围的小区域确定像素的阈值。
因此，对于同一图像的不同区域，我们获得了不同的阈值，从而为光照度变化的图像提供了更好的结果。
除上述参数外，方法cv.adaptiveThreshold还采用三个输入参数：
adaptiveMethod决定如何计算阈值：
cv.ADAPTIVE_THRESH_MEAN_C：该阈值是邻域平均值减去常数C。
cv.ADAPTIVE_THRESH_GAUSSIAN_C ：此阈值是邻域值的高斯加权总和减去常数C。
其中，邻域的大小由blockSize确定，C是从邻域像素的平均值或加权总和中减去的常数。
"""
# img = cv.imread('sudoku2.png', 0)
"""
使用中值滤镜模糊图像。
该功能使用具有ksize×ksize光圈的中值滤波器对图像进行平滑处理。
"""
# img = cv.medianBlur(img, 5)
# ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# 参数 src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]
# th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
#                            cv.THRESH_BINARY, 11, 2)
# th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
#                            cv.THRESH_BINARY_INV, 11, 2)
# titles = ['Original Image', 'Global Thresholding (v = 127)',
#           'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
# for i in range(4):
#     plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()

"""
Otsu's Binarization 二值化

在全局阈值化中，我们使用任意选择的值作为阈值。
相反，Otsu的方法避免了必须选择一个值并自动确定它的情况。
考虑仅具有两个不同图像值的图像（双峰图像），其中直方图将仅包含两个峰。
一个好的阈值应该在这两个值的中间。
类似地，Otsu的方法从图像直方图中确定最佳全局阈值。
为此，使用了cv.threshold（）函数，其中cv.THRESH_OTSU作为附加标志传递。
阈值可以任​​意选择。
然后，算法找到最佳阈值，该阈值作为第一输出返回。
查看以下示例。
输入图像为噪点图像。
在第一种情况下，将应用值127的全局阈值。
在第二种情况下，将直接应用Otsu的阈值。
在第三种情况下，首先使用5x5高斯核对图像进行滤波以去除噪声，然后应用Otsu阈值处理。
了解噪声过滤如何改善结果。
"""

img = cv.imread('sudoku2.png', 0)
# global thresholding
ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# Otsu's thresholding
ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur(img, (9, 7), 0)  # 长宽必须奇数！
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
plt.show()
