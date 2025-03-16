import cv2
import numpy as np
import imutils

image_s = cv2.imread("src/sauron.jpg")



cv2.namedWindow("Sauron original")
cv2.imshow("Sauron original", image_s)

# use imutils function to rotate an image 180 degrees
# rotate our image by 33 degrees counterclockwise, ensuring the
# entire rotated image still renders within the viewing area
rotated = imutils.rotate_bound(image_s, -33)
cv2.imshow("Rotated Without Cropping", rotated)

cv2.waitKey(0)


cv2.destroyAllWindows()