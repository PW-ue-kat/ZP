import cv2
import numpy as np
import imutils

image_s = cv2.imread("src/sauron.jpg")



cv2.namedWindow("Sauron original")
cv2.imshow("Sauron original", image_s)

angle = 0

for i in range (25):

    rotated=imutils.rotate_bound(image_s, angle)
    cv2.imshow(f"Rotated by {angle} Degrees", rotated)
    cv2.waitKey(500)
    angle += 15

cv2.waitKey(0)
cv2.destroyAllWindows()