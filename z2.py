# import the necessary packages
import numpy as np
import cv2
# initialize our canvas as a 300x300 pixel image with 3 channels
# (Red, Green, and Blue) with a black background
canvas = np.zeros((400, 400, 3), dtype="uint8")

blue = (255,0,0)
red = (0,0, 255)
green = (0, 255,0)
cv2.imshow("Original", canvas)
# Zielony prostokąt o wymiarach 100x50 pikseli w lewym górnym rogu.
cv2.rectangle(canvas, (0,0),(100,50),green)
cv2.imshow("Green", canvas)
# Czerwony prostokąt o grubości 3 px w prawym dolnym rogu.

(h, w) = canvas.shape[:2]

cY = (h//2)
cX = (w//2)

cv2.rectangle(canvas, (cX,cY),(w-1,h-1),red,3)

cv2.imshow("Changed", canvas)

cv2.waitKey(0)