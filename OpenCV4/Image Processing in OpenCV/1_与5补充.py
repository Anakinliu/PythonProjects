
import cv2 as cv
import numpy as np
"""
# 使用Erosion补充，去除小的白色噪点
"""
while True:
    # Take each frame
    img = cv.imread('find_blue.jpg')

    # Convert BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    kernel = np.ones((3, 3), np.uint8)
    # mask_remove_noisy = cv.erode(mask, kernel, iterations=1)
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(img, img, mask=opening)
    cv.imshow('frame', img)
    cv.imshow('mask', mask)
    cv.imshow('opening', opening)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
