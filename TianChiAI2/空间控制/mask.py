import cv2 as cv
img = cv.imread('./real-house-mask.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img_gray, 220, 255, cv.THRESH_BINARY)

# cv.imshow('gray', img_gray)
cv.imshow('mask', mask)
cv.waitKey(0)