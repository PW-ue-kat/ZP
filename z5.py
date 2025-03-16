import cv2
import numpy as np
import imutils

image_s = cv2.imread("src/sauron.jpg")



cv2.namedWindow("Sauron original")
cv2.imshow("Sauron original", image_s)

# use imutils function to rotate an image 180 degrees
rotated = imutils.rotate(image_s, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)

cv2.waitKey(0)


cv2.destroyAllWindows()