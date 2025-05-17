# import the necessary packages
import numpy as np
import cv2
# initialize our canvas as a 300x300 pixel image with 3 channels
# (Red, Green, and Blue) with a black background
canvas = np.zeros((300, 300, 3), dtype="uint8")

blue = (255,0,0)
red = (0,0, 255)
green = (0, 255,0)
cv2.imshow("Original", canvas)
#Niebieski okrąg o promieniu 40 px w lewym górnym rogu.
cv2.circle(canvas,(40,40),40, blue)
#Czerwony okrąg o promieniu 60 px w środku obrazu.
(h, w) = canvas.shape[:2]
cY = (h//2)
cX = (w//2)

cv2.circle(canvas,(cX,cY),60, red)

cv2.imshow("Changed", canvas)

cv2.waitKey(0)