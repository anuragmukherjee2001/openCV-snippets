import cv2

# importing the image as grayscale image
img = cv2.imread("images/img2.jpg",0)
cv2.imshow("Original image", img)
cv2.waitKey(0)

# converting the image to binary image
ret, binary_image = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)

cv2.destroyAllWindows()