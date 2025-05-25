import cv2
import numpy as np
import imutils

image_b = cv2.imread("src/balrog2_small.jpg")

(h, w) = image_b.shape[:2]
print(f'shape: {h},{w}')

cv2.imshow("Original", image_b)
# perform the resizing

scaled_h = int(h*3)
scaled_w = int(w*3)



resized = imutils.resize(image_b, width=800)

cv2.imshow("Resized", resized)

cv2.imwrite("src/resized_output.jpg", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

