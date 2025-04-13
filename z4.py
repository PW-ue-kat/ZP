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

methods = [
("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
# loop over the interpolation methods
for (name, method) in methods:
# increase the size of the image by 3x using the current
# #Zmiana rozmiaru 3

# interpolation method
    print("[INFO] {}".format(name))
    resized = imutils.resize(image_b, width=image_b.shape[1] * 3,
    inter=method)
    cv2.imshow("Method: {}".format(name), resized)


cv2.waitKey(0)
cv2.destroyAllWindows()