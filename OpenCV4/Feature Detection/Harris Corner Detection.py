"""
 @Description      
 @author          linux
 @create          2020-05-21 16:00
"""
import numpy as np
import cv2 as cv

filename = 'cy.jpeg'
img = cv.imread(filename)
# print(type(img))  # <class 'numpy.ndarray'>
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
cv.imshow('gray', gray)

dst = cv.cornerHarris(gray, 2, 3, 0.04)
cv.imshow('dst', dst)

# 扩大标记点的大小，不重要
dst = cv.dilate(dst, None)

cv.imshow('dilated-dst', dst)
# 最佳值的阈值可能会因图像而异。
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv.imshow('img', img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
