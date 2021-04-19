import cv2

img = cv2.imread("images/img3.jpg")
cv2.imshow("Original Image", img)
cv2.waitKey(0)

img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV colour", img_HSV)
cv2.waitKey(0)

cv2.imshow("Hue channel", img_HSV[:, :, 0])
cv2.waitKey(0)

cv2.imshow("Saturation channel", img_HSV[:, :, 1])
cv2.waitKey(0)

cv2.imshow("value channel", img_HSV[:, :, 2])
cv2.waitKey(0)

cv2.destroyAllWindows()
