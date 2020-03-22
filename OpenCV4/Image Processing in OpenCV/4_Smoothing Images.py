"""
学习到：
1. 使用各种低通滤镜模糊图像
2. 将定制滤镜应用于图像（2D卷积）
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

"""
2D Convolution ( Image Filtering )

可以使用各种低通滤波器（LPF），高通滤波器（HPF）等对图像进行filter。
LPF有助于去除噪声，模糊图像等。HPF滤波器有助于在图像中查找边缘。

OpenCV提供了一个函数cv.filter2D（）来将内核与映像进行卷积。
例如，我们将尝试对图像进行平均滤波。 
5x5平均滤波器内核如下所示：

该操作如下：将内核保持在一个像素上方，将所有25个像素加到该内核下方，取平均值，然后将中心像素替换为新的平均值。
对于图像中的所有像素，将继续执行此操作。
"""
# plt_img = mpimg.imread('virus.png')

# img = cv.imread('virus.png')
# print(img)
# print(plt_img)
# plt.subplot(131), plt.imshow(plt_img), plt.title('Original')
# plt.xticks([]), plt.yticks([])
# kernel = np.ones((5, 5), np.float32) / 25
# bigger_kernel = np.ones((8, 10), np.float32) / 80  # 不必是奇数
"""
该函数将任意线性滤波器应用于图像。
支持就地操作。
当光圈部分位于图像外部时，该函数会根据指定的边框模式对异常像素值进行插值。
该函数实际上会计算相关性，而不是卷积：
在内核足够大（〜11 x 11或更大）的情况下，该函数使用基于DFT的算法，而对于小内核则使用直接算法。
"""
# dst1 = cv.filter2D(plt_img, -1, kernel)
# dst2 = cv.filter2D(plt_img, -1, bigger_kernel)
#
#
# plt.subplot(132), plt.imshow(dst1), plt.title('Averaging')
# plt.subplot(133), plt.imshow(dst2), plt.title('big')
# plt.xticks([]), plt.yticks([])
# plt.show()

# ---------------

"""
图像模糊（图像平滑）

通过将图像与低通滤波器内核进行卷积来实现图像模糊。
这对于消除噪音很有用。
它实际上从图像中去除了高频内容（例如，噪声，边缘）。
因此在此操作中边缘稍微模糊了（还有一些模糊技术不会使边缘模糊）。 
OpenCV提供了四种主要的模糊技术。
"""

"""
1. Averaging
取均值
这是通过将图像与规范化的框滤镜（normalized box filter）进行卷积来完成的。
它仅获取内核kernel区域下所有像素的平均值，并替换中心元素。
这是通过功能cv.blur（）或cv.boxFilter（）完成的。
检查文档以获取有关内核的更多详细信息。
我们应该指定内核的宽度和高度。
2. 高斯模糊
3. 中位数模糊
"""
# img = cv.imread('median.png')
# box_blur = cv.blur(img, (2, 2))
# box_no_normalize_blur = cv.boxFilter(src=img, ddepth=-1, ksize=(2, 2), normalize=False)
# median_blur = cv.medianBlur(img, 5)
# plt.subplot(221), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('原始')
# plt.xticks([]), plt.yticks([])
# plt.subplot(222), plt.imshow(cv.cvtColor(box_blur, cv.COLOR_BGR2RGB)), plt.title('简单box模糊')
# plt.xticks([]), plt.yticks([])
# plt.subplot(223), plt.imshow(cv.cvtColor(box_no_normalize_blur, cv.COLOR_BGR2RGB)), plt.title('简单非normalize box模糊')
# plt.xticks([]), plt.yticks([])
# plt.subplot(224), plt.imshow(cv.cvtColor(median_blur, cv.COLOR_BGR2RGB)), plt.title('中位数模糊')
# plt.xticks([]), plt.yticks([])
# plt.show()

"""
4. Bilateral Filtering  

"""
img = cv.imread('bil.png')
box_blur = cv.blur(img, (2, 2))
bil = cv.bilateralFilter(img, 9, 750, 750)
med_blur = cv.medianBlur(img, 7)
plt.subplot(221), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('原始')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(cv.cvtColor(box_blur, cv.COLOR_BGR2RGB)), plt.title('简单box模糊')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(cv.cvtColor(bil, cv.COLOR_BGR2RGB)), plt.title('bil 模糊')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(cv.cvtColor(med_blur, cv.COLOR_BGR2RGB)), plt.title('中位数模糊')
plt.xticks([]), plt.yticks([])
plt.show()
