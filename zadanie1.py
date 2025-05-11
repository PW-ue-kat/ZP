# import the necessary packages
import numpy as np
import cv2

original = cv2.imread("src/hokej.jpg")

(B, G, R) = cv2.split(original)

cv2.imshow("Original", original)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.imwrite("src/hokej_red.jpg", R)
cv2.imwrite("src/hokej_blue.jpg", B)
cv2.imwrite("src/hokej_green.jpg", G)


cv2.waitKey(0)
cv2.destroyAllWindows()
