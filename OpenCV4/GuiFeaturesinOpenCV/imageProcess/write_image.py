import numpy as np
import cv2 as cv

my_img1 = cv.imread('gun.jpg', 1)
my_img2 = cv.imread('gun.jpg', 0)
my_img3 = cv.imread('gun.jpg', -1)

cv.namedWindow('1', cv.WINDOW_NORMAL)
cv.namedWindow('0', cv.WINDOW_NORMAL)
cv.namedWindow('-1', cv.WINDOW_NORMAL)
cv.imshow('1', my_img1)
cv.imshow('0', my_img2)
cv.imshow('-1', my_img3)

cv.imwrite('RGB1.png', my_img1)
cv.imwrite('GRAY0.png', my_img2)
cv.imwrite('RGBA-1.png', my_img3)

cv.waitKey(0)
cv.destroyAllWindows()