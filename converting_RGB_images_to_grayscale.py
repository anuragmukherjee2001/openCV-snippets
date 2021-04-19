import cv2

img = cv2.imread("images/img1.jpg")
cv2.imshow("Normal image", img)
cv2.waitKey(0)

# first process
gray_scale_image = cv2.imread("images/img1.jpg", 0)
cv2.imshow("Gray scale Image", gray_scale_image)
cv2.waitKey(0)

# second process
gray_image_2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_image2", gray_image_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
