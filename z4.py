import cv2
import numpy as np
import imutils

image_s = cv2.imread("src/sauron.jpg")

(h, w) = image_s.shape[:2]
(cX, cY) = (w // 2, h // 2)



x = int(input("Podaj kat obrotu:"))

cv2.namedWindow("Sauron original")
cv2.imshow("Sauron original", image_s)


# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), x, 1.0)
rotated = cv2.warpAffine(image_s, M, (w, h))
cv2.imshow(f"Rotated by {x} Degrees", rotated)

cv2.waitKey(0)

cv2.destroyAllWindows()

