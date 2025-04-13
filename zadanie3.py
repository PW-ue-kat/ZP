import cv2
import numpy as np

image_w = cv2.imread("src/wywern.jpg")

M = np.ones(image_w.shape, dtype="uint8")*80


added = cv2.subtract(image_w, M)
cv2.imshow("Original", image_w)
cv2.imshow("Darker_cv", added)

added_np = image_w - M
cv2.imshow("Darker_np", added_np)

cv2.waitKey(0)
cv2.destroyAllWindows()


