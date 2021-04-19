import cv2
import numpy as np

img = cv2.imread("images/img3.jpg")
cv2.imshow("Original Image", img)
cv2.waitKey(0)

height, width = img.shape[:2]
print(height)
print(width)

# setting the dimensions of the new image into a variable
decreased_height, decreased_width = height / 4, width / 4
print(decreased_height)
print(decreased_width)

# creating the translation matrix
T_matrix = np.float32([[1, 0, decreased_width],
                       [0, 1, decreased_height]
                       ])

print(T_matrix)

# creating the translated image
img_translation = cv2.warpAffine(img, T_matrix, (width, height))
cv2.imshow("Created image", img_translation)
cv2.waitKey(0)

cv2.destroyAllWindows()
