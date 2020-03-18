import numpy as np
import cv2 as cv
cap = cv.VideoCapture('../source/15s.mkv')

# 获取尺寸
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(f'高{height}宽{width}')

# 定义codec ，创建VideoWriter对象
fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (width, height))

while cap.isOpened():
    ret, a_frame = cap.read()  # 迭代读取帧，读到最后，返回（false，None）
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (maybe stream end?). Exiting ...")
        break
    # gray = cv.cvtColor(a_frame, code=cv.COLOR_RGB2GRAY)  #  RGB？？
    frame_flipped = cv.flip(a_frame, -9)
    out.write(frame_flipped)  # 写出帧
    cv.imshow('WTF?', frame_flipped)
    # print('showing...')  # 一直
    # wait as least 100 mills,25 is OK
    if cv.waitKey(1) == ord('q'):
        break
cap.release()  # 后续不再open所以需要手动关闭，open里自带release
out.release()  # 释放资源
cv.destroyAllWindows()