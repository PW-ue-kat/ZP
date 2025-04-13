import cv2
import numpy as np

image_k = cv2.imread("src/karolak.jpeg")

roi = image_k[:100, :100]

cv2.imshow("ROI",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


