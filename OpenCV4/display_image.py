import numpy as np
import cv2 as cv

# ndarray
img = cv.imread('gun.jpg', -1)
# 如果读入错误，没有提示，但是print img 为None


cv.namedWindow('m4', cv.WINDOW_NORMAL)  # cv.WINDOW_NORMAL自定义窗口大小
cv.imshow('m4', img)
cv.waitKey(0)  # 执行完此语句才会显示图形，多少秒后自动关闭,0不关闭
# cv.destroyAllWindows()
cv.destroyWindow('m4')
