import cv2

img = cv2.imread("images/img3.jpg")
cv2.imshow("Original Image", img)
cv2.waitKey(0)

small_image = cv2.pyrDown(img)
cv2.imshow("Small Image", small_image)
cv2.waitKey(0)

large_image = cv2.pyrUp(img)
cv2.imshow("Large Image", large_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
