import cv2
import numpy as np

image_k = cv2.imread("src/karolak2.jpg")

(h, w, c) = image_k.shape[:3]

roi_upper = image_k[:int(h/2), :]
roi_lower = image_k[int(h/2):, :]

cv2.imshow("ROI_upper",roi_upper)
cv2.imshow("ROI_lower",roi_lower)
cv2.waitKey(0)
cv2.destroyAllWindows()


