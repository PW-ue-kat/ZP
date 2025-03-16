import cv2
import numpy as np
import imutils

image_m = cv2.imread("src/morgoth.jpg")



cv2.namedWindow("Morgoth original")
cv2.imshow("Morgoth original", image_m)


shifted = imutils.translate(image_m, 100, 50)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)


cv2.destroyAllWindows()