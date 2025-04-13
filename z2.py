import cv2
import numpy as np

image_b = cv2.imread("src/balrog2.jpg")

(h, w) = image_b.shape[:2]
print(f'channels: {h},{w}')

cv2.imshow("Original", image_b)
# perform the resizing

double_h = int(h*2)
double_w = int(w*2)


resized = cv2.resize(image_b, (double_w, double_h), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()