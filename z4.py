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

#Czerwony okrąg o promieniu 60 px w środku obrazu.
(h, w) = canvas.shape[:2]
cY = (h//2)
cX = (w//2)
#kwadratu o wymiarach 100x100
cv2.rectangle(canvas,(cX-50,cY-50),(cX+50,cY+50),red,3)
#wewnątrz którego znajduje się mniejszy okrąg o promieniu 30 px.
cv2.circle(canvas,(cX,cY),30, green,2)

cv2.imshow("Changed", canvas)

cv2.waitKey(0)