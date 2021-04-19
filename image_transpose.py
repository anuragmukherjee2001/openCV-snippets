import cv2

img = cv2.imread("images/img3.jpg")
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# rotating the image by 90 degrees without loosing any information
rotated_image = cv2.transpose(img)
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)

cv2.destroyAllWindows()