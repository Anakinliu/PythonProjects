import numpy as np
import cv2
import matplotlib.pyplot as plt

# 图6-1中的矩阵
img = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],qqq
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
], dtype=np.uint8)

# 用matplotlib存储 RGB 顺序
plt.imsave('./img_pyplot.png', img)

# 用OpenCV存储 BGR 顺序
cv2.imwrite('./img_cv2.png', img)