import cv2
import numpy as np
import imutils

image_s = cv2.imread("src/sauron.jpg")



cv2.namedWindow("Sauron original")
cv2.imshow("Sauron original", image_s)

# entire rotated image still renders within the viewing area
rotated = imutils.rotate_bound(image_s, 75)
cv2.imshow("Rotated Without Cropping", rotated)
cv2.imwrite('src/rotated_output.jpg',rotated)
cv2.waitKey(0)


cv2.destroyAllWindows()