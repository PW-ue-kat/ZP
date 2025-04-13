import cv2
import numpy as np

image_k = cv2.imread("src/karolak2.jpg")

roi = image_k[:300, :300]

cv2.imshow("ROI",roi)
cv2.imwrite("src/cropped300.jpg",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()