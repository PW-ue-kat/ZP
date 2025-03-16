import cv2
import numpy as np
import imutils

image_s = cv2.imread("src/sauron.jpg")



cv2.namedWindow("Sauron original")
cv2.imshow("Sauron original", image_s)

# use imutils function to rotate an image 180 degrees
rotated90 = imutils.rotate(image_s, 90)
cv2.imshow("Rotated by 90 Degrees", rotated90)

rotated3x30 = image_s
for i in range (3):
    rotated3x30=imutils.rotate(rotated3x30, 30)

cv2.imshow("Rotated by 3x30 Degrees", rotated3x30)
cv2.waitKey(0)


cv2.destroyAllWindows()