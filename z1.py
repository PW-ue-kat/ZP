import cv2
import numpy as np

image_b = cv2.imread("src/balrog.jpg")

(h, w, c) = image_b.shape[:3]
print(f'channels: {h},{w},{c}')

cv2.imshow("Original", image_b)
# perform the resizing

half_h = h/2
half_w = w/2


resized = cv2.resize(image_b, (int(half_w), int(half_h)), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()