import cv2
import numpy as np

image_w = cv2.imread("src/wywern.jpg")

M = np.ones(image_w.shape, dtype="uint8")*150


added = cv2.add(image_w, M)
cv2.imshow("Original", image_w)
cv2.imshow("Lighter_cv", added)

added_np = image_w + M
cv2.imshow("Lighter_np", added_np)

cv2.waitKey(0)
cv2.destroyAllWindows()


