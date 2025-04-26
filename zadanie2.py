import numpy as np
import cv2

image = cv2.imread("src/stolik.png")

cv2.imshow("Original", image)


mask = np.zeros(image.shape[:2], dtype="uint8")
#cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)

cv2.ellipse(mask,
           center=(135, 120),
           axes=(15, 8),
           angle=0,
           startAngle=0,
           endAngle=360,
           color=255,
           thickness=-1)
cv2.imshow("Ellipse Mask", mask)


masked = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
cv2.imshow("Negative Mask Applied to Image", masked)

cv2.waitKey()
cv2.destroyAllWindows()