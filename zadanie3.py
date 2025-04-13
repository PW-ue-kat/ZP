import cv2
import numpy as np

image_k = cv2.imread("src/karolak2.jpg")

(h, w, c) = image_k.shape[:3]

roi_left = image_k[:, :int(w/2)]
roi_right = image_k[:, int(w/2):]

cv2.imshow("ROI_upper",roi_left)
cv2.imshow("ROI_lower",roi_right)
cv2.waitKey(0)
cv2.destroyAllWindows()


