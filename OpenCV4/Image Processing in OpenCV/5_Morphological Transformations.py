"""
在本章中，我们将学习不同的形态学操作，例如侵蚀，膨胀，打开，关闭等。
我们将看到不同的函数，例如：cv.erode（），cv.dilate（），cv.morphologyEx（）等。

形态变换是一些基于图像形状的简单操作。
通常在二进制图像上执行。
它需要两个输入，一个是我们的原始图像，第二个是决定操作性质的结构元素或内核。
两种基本的形态学算子是侵蚀和膨胀Erosion and Dilation。
然后，它的变体形式（如“打开”，“关闭”，“渐变Gradient ”等）。

"""
import cv2 as cv
import numpy as np

img = cv.imread('j.png', 0)
"""
1. Erosion
侵蚀的基本思想就像仅是土壤侵蚀一样，它侵蚀了前景物体的边界（始终尝试使前景保持白色）。
那是什么呢？
内核在图像中滑动（如上一章的2D卷积）。
仅当内核下的所有像素均为1时，原始图像中的像素（1或0）才被视为1，否则它将被侵蚀（设为零）。

根据内核的大小，边界附近的所有像素都将被丢弃。
因此，前景对象的厚度或大小会减小，或者图像中的白色区域只会减小。
这对于消除小的白噪声（如我们在色彩空间一章中看到的），分离两个连接的对象等非常有用。
"""
# kernel = np.ones((5, 5), np.uint8)
# kernel_big = np.ones((7, 7), np.uint8)
# erosion = cv.erode(img, kernel, iterations=1)
# erosion_big_kernel = cv.erode(img, kernel_big, iterations=1)
# erosion_big_kernel = cv.erode(img, kernel_big, iterations=1)
# cv.imshow('original', img)
# cv.imshow('erosion', erosion)
# cv.imshow('erosion_big', erosion_big_kernel)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
2. Dilation

它与侵蚀正好相反。
如果内核下的至少一个像素为“ 1”，则像素元素为“ 1”。
因此，它会增加图像中的白色区域或增加前景对象的大小。
通常，在消除噪音的情况下，腐蚀后会膨胀。
因为腐蚀会消除白噪声，但也会缩小物体。
因此，我们对其进行了扩展。
由于噪音消失了，它们不会回来，但我们的目标区域增加了。
在连接对象的损坏部分时也很有用。

"""
# kernel = np.ones((5, 5), np.uint8)
# dilation = cv.dilate(img, kernel, iterations=1)
# cv.imshow('original', img)
# cv.imshow(' increases the white region', dilation)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
3. Opening

dilation之后再erosion的一个别称. 效果很好
"""
# img3 = cv.imread('j3.png')
# kernel = np.ones((5, 5), np.float32)
# opening = cv.morphologyEx(img3, cv.MORPH_OPEN, kernel)
# erosion = cv.erode(img3, kernel, iterations=1)
# cv.imshow('opening', opening)
# cv.imshow('original', img3)
# cv.imshow('erosion', erosion)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
4. closing 
erosion之后再dilation
"""
# img4 = cv.imread('j4.png')
# kernel = np.ones((5, 5), np.float32)
# closing = cv.morphologyEx(img4, cv.MORPH_CLOSE, kernel)
# cv.imshow('closing', closing)
# cv.imshow('original', img4)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
5. Morphological Gradient
与扩张和腐蚀都不同。
结果看起来像对象的轮廓。

"""

# kernel = np.ones((2, 2), np.float32)
# bigger_kernel = np.ones((5, 5), np.float32)
# gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
# big_kernel_gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, bigger_kernel)
# cv.imshow('gradient', gradient)
# cv.imshow('bigger_gradient', big_kernel_gradient)
# cv.imshow('original', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
还有6. Top Hat 和7. black hat
"""

"""
自定义kernel性形状，不再是单一的矩形


在Numpy的帮助下，我们在前面的示例中手动创建了一个结构元素。
它是矩形。
但是在某些情况下，您可能需要椭圆形/圆形的内核。
因此，为此，OpenCV具有一个函数
cv.getStructuringElement（）。
您只要传递内核的形状和大小，就可以得到所需的内核。
"""
# Rectangular Kernel
cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
# array([[1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1]], dtype=uint8)
# Elliptical Kernel
cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
# array([[0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [0, 0, 1, 0, 0]], dtype=uint8)
# Cross-shaped Kernel
cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
# array([[0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1],
#        [0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0]], dtype=uint8)

kernel = np.ones((2, 2), np.float32)
bigger_kernel = np.ones((5, 5), np.float32)
ell_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
big_kernel_gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, bigger_kernel)
# 对比同样5x5的bigger_kernel看起来粗细更加均匀
ell_kernel_gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, ell_kernel)

cv.imshow('gradient', gradient)
cv.imshow('bigger_gradient', big_kernel_gradient)
cv.imshow('ell_kernel_gradient', ell_kernel_gradient)
cv.imshow('original', img)
cv.waitKey(0)
cv.destroyAllWindows()
