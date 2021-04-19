import cv2

img = cv2.imread("images/img1.jpg", -1)

copied_part = img[200:300, 200:300]
img[50:150, 400:500] = copied_part

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()