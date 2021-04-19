import cv2 as cv
import numpy as np

# Reading Videos in opencv

capture = cv.VideoCapture('videos/vid1.mp4')

while True:
    isTrue, frame = capture.read()
    image = np.zeros()

    cv.imshow('video', frame)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
