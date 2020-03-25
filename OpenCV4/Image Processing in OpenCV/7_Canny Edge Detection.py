"""
在这一章中，我们将学习

Canny 边缘检测的概念
cv.Canny() Cv. Canny ()

"""

"""
Canny 边缘检测算法是一种流行的边缘检测算法,John F. Canny 提出
需要多个阶段
1. 消除噪声
由于边缘检测容易受到图像中的噪声，第一步是用5x5高斯滤波器去除图像中的噪声。 我们已经在前面的章节中看到了这一点。
2. 查找图像的强度梯度Intensity Gradient
然后使用Sobel核在水平和垂直方向上对平滑的图像进行滤波，以在水平方向（Gx）和垂直方向（Gy）上获得一阶导数。
从这两张图片中，我们可以找到每个像素的边缘渐变和方向，如下所示：
Edge_Gradient(G)=sqrt((Gx)^2 + (Gy)^2) 
Angle(θ)=(tan^−1)(Gy / Gx)
梯度方向始终垂直于边缘。
将其舍入为代表垂直，水平和两个对角线方向的四个角度之一。
3. 非最大抑制
在获得梯度大小和方向后，将对图像进行全面扫描，以去除可能不构成边缘的所有不需要的像素。
为此，在每个像素处，检查像素是否是其在梯度方向上附近的局部最大值。
图片在https://docs.opencv.org/master/da/d22/tutorial_py_canny.html
4. Hysteresis Thresholding
该阶段确定哪些边缘全部是真正的边缘，哪些不是。
为此，我们需要两个阈值minVal和maxVal。
强度梯度大于maxVal的任何边缘必定是边缘，
而小于minVal的那些边缘必定是非边缘，因此将其丢弃。
介于这两个阈值之间的对象根据其连通性被分类为边缘或非边缘。
如果它们连接到“必定是边缘”的像素，则将它们视为边缘的一部分。
否则，它们也将被丢弃。
见下图：图片在https://docs.opencv.org/master/da/d22/tutorial_py_canny.html
选择合适的阈值很重要

因此，我们最终得到的是图像中的强边缘。

"""

"""
Canny Edge Detection in OpenCV
OpenCV将以上所有内容放在单个函数cv.Canny（）中。
我们将看到如何使用它。
第一个参数是我们的输入图像。
第二个和第三个参数分别是我们的minVal和maxVal。
第三个参数是perture_size。它是用于查找图像渐变的Sobel内核的大小。默认情况下为3。
最后一个参数是L2gradient，它指定用于查找梯度幅度的方程式。
如果为True，则使用上述更精确的公式，否则使用以下函数：Edge_Gradient（G）= | Gx | + | Gy |。
默认情况下，它为False。
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('dog2.png', 0)


def track(th1, th2):
    edges = cv.Canny(img, th1, th2)
    cv.imshow(f'{th1} -- {th2}', edges)
    cv.waitKey(0)


for i in range(20):
    track(100, 200 + i * 10)
cv.destroyAllWindows()
