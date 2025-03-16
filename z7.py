import cv2
import numpy as np
import imutils

image_s = cv2.imread("src/sauron.jpg")



cv2.namedWindow("Sauron original")
cv2.imshow("Sauron original", image_s)

# use imutils function to rotate an image 180 degrees
rotated_imutils = imutils.rotate(image_s, 45)
cv2.imshow("Rotated by 45 Degrees imutils", rotated_imutils)
#------- warpAffine
(h, w) = image_s.shape[:2]
(cX, cY) = (w // 2, h // 2)





# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated_warpAffine = cv2.warpAffine(image_s, M, (w, h))
cv2.imshow("Rotated by 45 Degrees warpAffine", rotated_warpAffine)

cv2.waitKey(0)


cv2.destroyAllWindows()