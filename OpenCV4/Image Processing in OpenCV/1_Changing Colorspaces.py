"""

学习如何将图像从一种颜色空间转换为另一种颜色空间，例如BGR↔Gray，BGR↔HSV等。
此外，我们还将创建一个应用程序来提取视频中的彩色对象。
将学习以下功能：cv.cvtColor（），cv.inRange（）等。
"""
import cv2 as cv
import numpy as np

"""
change Color-Space

OpenCV提供了150多种颜色空间转换方法,
最常用的BGR↔Gray，BGR↔HSV

使用函数cv.cvtColor（input_image，flag），其中flag确定转换类型。

对于HSV，色相范围为[0,179]，饱和度范围为[0,255]，值范围为[0,255]。
不同的软件使用不同的比例。
因此，如果将OpenCV值与它们进行比较，则需要将这些范围标准化。
"""
# 颜色空间转换方法
# flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# print(flags)

# 对于BGR→灰色转换，我们使用标志cv.COLOR_BGR2GRAY。
# img = cv.imread('virus.png')
# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 同样，对于BGR→HSV，我们使用标志cv.COLOR_BGR2HSV。
# img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('gray', img_gray)
# cv.imshow('hsv', img_hsv)
# cv.waitKey(0)
# cv.destroyAllWindows()

"""
物体跟踪

现在我们知道如何将BGR图像转换为HSV，我们可以使用它来提取有色对象。
在HSV中，表示颜色要比在BGR颜色空间中表示容易。
在我们的应用程序中，我们将尝试提取一个蓝色的对象。
所以这是方法：
- 截图视频的每一帧
- 转换BGR为HSV
- 我们将HSV图片的阈值范围设为想要的物体的颜色区间
- 提取物体
"""


cap = cv.VideoCapture('./green_pen.mp4')
while cap.isOpened():
    # Take each frame
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (maybe stream end?). Exiting ...")
        break
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    # 检测笔帽。。。
    lower_green = np.array([60, 230, 190])
    upper_green = np.array([80, 255, 210])
    # 同时找笔杆
    lower_black = np.array([100, 30, 10])
    upper_black = np.array([150, 100, 100])
    # 74, 255, 206  BGR
    # Threshold the HSV image to get only blue colors
    # print(hsv.shape)  # (720, 1280, 3)
    print(hsv[0][0])
    # 检测每一个像素是否在区间内，是的话取值255，否则0
    mask_bi_mao = cv.inRange(hsv, lower_green, upper_green)
    mask_bi_gan = cv.inRange(hsv, lower_black, upper_black)
    # 使用cv的加法，在Core Operation中有介绍
    mask = cv.add(mask_bi_gan, mask_bi_mao)
    # print(mask.shape)  # (720, 1280) 灰度图像
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('hsv', hsv)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()
"""
图像中有一些噪点。
我们将在后面的章节中看到如何删除它。
这是对象跟踪中最简单的方法。
一旦学习了轮廓的功能，您就可以做很多事情，例如找到对象的质心并使用它来跟踪对象，仅通过将手放在相机前面就可以绘制图以及其他有趣的东西。

关键是，如何找到要追踪的HSV值？
"""

"""
这是在stackoverflow.com中发现的常见问题。
这非常简单，您可以使用相同的函数cv.cvtColor（）。
无需传递图像，只需传递所需的BGR值即可。
例如，要查找Green的HSV值，请在Python终端中尝试以下命令：

>>> green = np.uint8([[[0,255,0 ]]])
>>> hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
>>> print( hsv_green )
[[[ 60 255 255]]]

现在，您分别将[H-10，100,100]和[H + 10，255，255]作为下限和上限。
除此方法外，您还可以使用GIMP等任何图像编辑工具或任何在线转换器来找到这些值，但不要忘记调整HSV范围。
"""
