"""
https://docs.opencv.org/master/d5/d0f/tutorial_py_gradients.html
在本章中，我们将学习：查找图像gradients，边缘等
我们将看到以下函数：cv.Sobel（），cv.Scharr（），cv.Laplacian（）等

OpenCV提供了三种类型的gradient filter或high-pass filter，即Sobel，Scharr和Laplacian。
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

"""
1. Sobel and Scharr Derivatives

Sobel操作是高斯平滑加微分运算的联合运算，因此它更抗噪声。
您可以指定要采用的导数方向，垂直或水平（分别通过参数yorder和xorder）。
您还可以通过参数ksize指定内核的大小。
如果ksize = -1，则使用3x3 Scharr滤波器，其效果要比3x3 Sobel滤波器更好。
请参阅文档以了解所使用的内核。

"""

"""
2. Laplacian Derivatives
它计算由关系式Δsrc=∂2src∂x2+∂2src∂y2给出的图像的拉普拉斯算子，其中使用Sobel导数找到每个导数。
如果ksize = 1，则使用以下内核进行过滤：
"""

"""
下面的代码在单个图中显示了所有运算符。
所有内核的大小均为5x5。
将输出图像的深度传递-1以得到np.uint8类型的结果。
"""

# img = cv.imread('sudoku2.png', 0)
# laplacian = cv.Laplacian(img, cv.CV_64F)
# # src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]
# sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
# sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
# print(laplacian.dtype)
# print(sobelx.dtype)
# plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# plt.show()

"""
在我们的最后一个示例中，输出数据类型为cv.CV_8U或np.uint8。
但这有一个小问题。
黑色到白色的过渡被视为正斜率（具有正值），而白色到黑色的过渡被视为负斜率（具有负值）。
因此，当您将数据转换为np.uint8时，所有负斜率均​​设为零。
简而言之，您会错丢失边缘信息

如果要检测两个边缘，更好的选择是将输出数据类型保留为更高的形式，例如cv.CV_16S，cv.CV_64F等，取其绝对值，然后转换回cv.CV_8U。
下面的代码演示了用于水平Sobel滤波器和结果差异的此过程。
"""
img = cv.imread('box.png', 0)
# Output dtype = cv.CV_8U
sobelx8u = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=1)
# Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
sobelx64f = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=1)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap='gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()
