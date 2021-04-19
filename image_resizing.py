import cv2

img = cv2.imread("images/img3.jpg")
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# linear interpolation - Shrinking the image
shrinked_image = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Scaling Linear interpolation", shrinked_image)
cv2.waitKey(0)

# Cubic_Interpolation
expanded_image = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Scaling Cubic interpolation", expanded_image)
cv2.waitKey(0)

# Area Interpolation
areal_expanded_image = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
cv2.imshow("Scaling Area interpolation", areal_expanded_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
