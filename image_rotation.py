import cv2

img = cv2.imread("images/img3.jpg")
cv2.imshow("Original Image", img)
cv2.waitKey(0)

height, width = img.shape[:2]
print(height)
print(width)

# getting the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 0.5)

# getting the rotated image
rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
