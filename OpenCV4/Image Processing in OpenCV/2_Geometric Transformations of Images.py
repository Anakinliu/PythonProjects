"""
目标
学习将不同的几何变换应用于图像，例如平移，旋转，仿射变换等。
"""
import numpy as np
import cv2 as cv

"""
OpenCV提供了两个转换函数cv.warpAffine和cv.warpPerspective，您可以使用它们执行各种转换。 
cv.warpAffine采用2x3转换矩阵，而cv.warpPerspective采用3x3转换矩阵作为输入。

https://www.matongxue.com/madocs/244.html
"""

"""
缩放

缩放只是调整图像的大小。
为此，OpenCV带有一个函数cv.resize（）。
图像的大小可以手动指定，也可以指定缩放比例。
使用了不同的插值方法。
首选插值方法是cv.INTER_AREA，用于缩小（shrinking）的interpolation，
而用cv.INTER_CUBIC（慢）和cv.INTER_LINEAR则用于放大的interpolation。
默认情况下，插值方法cv.INTER_LINEAR用于所有调整大小目的。
您可以使用以下两种方法之一来调整输入图像的大小：

https://www.matongxue.com/madocs/244.html
"""

img = cv.imread('virus.png')
import matplotlib.pyplot as plt

# cv.resize(	src, dsize[, dst[, fx[, fy[, interpolation]]]]	)
# res1 = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
# # OR
# height, width = img.shape[:2]
# res2 = cv.resize(img, (2 * width, 2 * height), interpolation=cv.INTER_LINEAR)
# res3 = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
# res4 = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
# cv.imshow('1', res1)
# cv.imshow('2', res2)
# cv.imshow('3', res3)
# cv.imshow('4', res4)
# cv.waitKey(0)
# cv.destroyAllWindows()


"""
位移

使用仿射变换改变图像位置
"""
print(img.shape)
rows, cols, _ = img.shape
# 为什么是float32呢？
M1 = np.float32([[1, 0, cols // 2], [0, 1, rows // 2]])
M2 = np.float32([[1, 0, -cols // 2], [0, 1, -rows // 2]])
M3 = np.float32([[1, 0, -cols // 2], [0, 1, rows // 2]])
M4 = np.float32([[1, 0, cols // 2], [0, 1, -rows // 2]])
# 参数M必须是2*3的矩阵
# dst1 = cv.warpAffine(img, M1, (cols, rows))
# dst2 = cv.warpAffine(img, M2, (cols, rows))
# dst3 = cv.warpAffine(img, M3, (cols, rows))
# dst4 = cv.warpAffine(img, M4, (cols, rows))
# cv.imshow('dst1', dst1)
# cv.imshow('dst2', dst2)
# cv.imshow('dst3', dst3)
# cv.imshow('dst4', dst4)
# cv.waitKey(0)
# cv.destroyAllWindows()


"""
旋转
图像旋转一个角度θ可以通过以下形式的变换矩阵实现
但是OpenCV提供了缩放旋转和可调整的旋转中心，因此您可以在自己喜欢的任何位置旋转。
修改后的变换矩阵为

https://www.matongxue.com/madocs/244.html
"""
# cols-1 and rows-1 are the coordinate limits.

# OpenCV帮你实现了变换过程
# M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)

# dstR = cv.warpAffine(img, M, (cols, rows))
# cv.imshow('dstR', dstR)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
仿射变换

在仿射变换中，原始图像中的所有平行线在输出图像中仍将平行。
为了找到变换矩阵，我们需要输入图像中的三个点以及它们在输出图像中的对应位置。
这三个点相对图像本身的位置并没有变化
然后cv.getAffineTransform将创建一个2x3矩阵，该矩阵将传递给cv.warpAffine。

"""
# img = cv.imread('drawing.png')
# rows, cols, ch = img.shape
# pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
# pts2 = np.float32([[10, 100], [200, 50], [150, 500]])

# src源图像中三角形顶点的坐标。
# dst目标图像中相应三角形顶点的坐标。
# OpenCV帮你实现了变换过程
# M = cv.getAffineTransform(src=pts1, dst=pts2)
#
# dst = cv.warpAffine(img, M, (cols, rows))
# plt.subplot(121), plt.imshow(img), plt.title('Input')
# plt.subplot(122), plt.imshow(dst), plt.title('Output')
# plt.show()

"""
透视变换

对于透视变换，您需要一个3x3变换矩阵。
即使在转换后，直线也将保持直线。
要找到此变换矩阵，您需要在输入图像上有4个点，在输出图像上需要相应的点。
在这4个点中，其中每3个不共线。
然后可以通过函数cv.getPerspectiveTransform找到转换矩阵。
然后将cv.warpPerspective应用于此3x3转换矩阵。
"""

img = cv.imread('sudoku.png')
rows, cols, ch = img.shape
pts1 = np.float32([[40, 40], [17, 240], [240, 240], [230, 40]])
pts2 = np.float32([[0, 0], [0, 300], [300, 300], [300, 0]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (300, 300))
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
