import cv2 as cv
import numpy as np

blank_img = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank_img)

blank_img[:] = 0, 255, 0
# cv.imshow("green", blank_img)

blank_img[300:400, 500:600] = 0, 255, 0
# cv.imshow("green_image", blank_img)

cv.waitKey(0)
