import cv2 as cv

# reading images in opencv

img = cv.imread('images/img1.jpg')
cv.imshow('Pic', img)

cv.waitKey(0)

# Reading Videos in opencv

capture = cv.VideoCapture('videos/vid1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
