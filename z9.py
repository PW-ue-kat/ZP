import cv2
import numpy as np
import imutils

image_b = cv2.imread("src/balrog2_small.jpg")

(h, w) = image_b.shape[:2]
print(f'shape: {h},{w}')

cv2.imshow("Original", image_b)
# perform the resizing


for i in range(11):
    skala = ((i*20)+100)
    new_width = int(w*(skala/100))
    resized = imutils.resize(image_b, width=new_width,inter=cv2.INTER_LINEAR)
    cv2.imshow("Skala: {}%".format(skala), resized)
    cv2.waitKey(500)



cv2.waitKey(0)
cv2.destroyAllWindows()