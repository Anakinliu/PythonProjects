"""
cv.pyrUp()  cv.pyrDown()
参考：http://pages.cs.wisc.edu/~csverma/CS766_09/ImageMosaic/imagemosaic.html
"""

"""
通常，我们使用的是一个固定大小的图像。 但在某些情况下，我们需要使用不同分辨率的(相同的)图像。 
例如，当搜索图像中的某些东西时，比如脸，我们不能确定该物体在所述图像中的大小。 
在这种情况下，我们需要创建一组具有不同分辨率的相同图像，并在所有图像中搜索对象。 
这些具有不同分辨率的图像集合称为图像金字塔(因为当它们保存在一个堆栈中时，最高分辨率的图像在底部，
最低分辨率的图像在顶部，它看起来像一个金字塔)。

更高级别(低分辨率)的高斯金字塔图像是通过移除低级别(高分辨率)图像中连续的行和列而形成的。 
然后利用底层5个像素对高斯权重的贡献形成高层像素。 
这样，一个 m, n 图像就变成了 m / 2, n / 2图像。 
所以面积减少到原来面积的四分之一。 它被称为Octave。 
同样的模式，我们继续向上金字塔(即，分辨率下降)。 
同样，在扩展的同时，每个层次的面积变成4倍。 
我们可以使用 cv.pyrDown ()和 cv.pyrUp ()函数查找高斯金字塔。
"""
import cv2 as cv

img = cv.imread('virus.png')
# 使图像模糊并降低采样率。
lower_reso = cv.pyrDown(img)
# cv.imshow('lower_reso', lower_reso)
# cv.imshow('lower_lower_reso', cv.pyrDown(lower_reso))
# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
一旦降低分辨率，您将丢失信息
"""
higher_reso = cv.pyrUp(lower_reso)
# cv.imshow('original', img)
# cv.imshow('lower_reso', lower_reso)
# cv.imshow('higher_reso', higher_reso)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
使用金字塔图片混合
"""

"""
拉普拉斯金字塔是由高斯金字塔形成的。 这并不是唯一的功能。 拉普拉斯金字塔图像只像边缘图像。 它的大部分元素都是0。 它们被用于图像压缩。 拉普拉斯金字塔中的一个水平是由拉普拉斯金字塔中的一个水平和拉普拉斯金字塔中的一个水平之间的差异形成的，拉普拉斯金字塔中的一个水平是由拉普拉斯金字塔中的一个高斯金字塔和拉普拉斯。 三个层次的拉普拉斯水平将看起来如下(对比度调整，以提高内容) :

您将需要将两个图像堆叠在一起，但是由于图像之间的不连续性，可能看起来不太好。
在这种情况下，使用“金字塔”进行图像融合可让您无缝融合，而不会在图像中留下大量数据。
"""
import numpy as np, sys

A = cv.imread('apple.png')
B = cv.imread('orange.png')
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)
# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)
# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i - 1], GE)
    lpA.append(L)
# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i - 1], GE)
    lpB.append(L)
# Now add left and right halves of images in each level
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols / 2], lb[:, cols / 2:]))
    LS.append(ls)
# now reconstruct
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])
# image with direct connecting each half
real = np.hstack((A[:, :cols / 2], B[:, cols / 2:]))
cv.imwrite('Pyramid_blending2.jpg', ls_)
cv.imwrite('Direct_blending.jpg', real)
