import cv2 as cv

img = cv.imread('images/img2.jpg')
cv.imshow('image', img)


def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


# Only work for live videos
def change_resolution(width, height):
    capture.set(3, width)
    capture.set(4, height)


resized_image = rescale(img)
cv.imshow('Image', resized_image)
cv.waitKey(0)

capture = cv.VideoCapture('videos/vid1.mp4')

while True:
    isTrue, frame = capture.read()

    resize_frame = rescale(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', resize_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
