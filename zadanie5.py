# import the necessary packages
import numpy as np
import cv2

original = cv2.imread("src/hokej.jpg")

(B, G, R) = cv2.split(original)

mask = np.zeros(original.shape[:2], dtype="uint8")

B = cv2.add(50, B)

mask = np.zeros(original.shape[:2], dtype="uint8")
#cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)

original.shape[:2]

cv2.ellipse(mask,
           center=(1400, 2400),
           axes=(300, 700),
           angle=0,
           startAngle=0,
           endAngle=360,
           color=255,
           thickness=-1)


merged = cv2.merge([B,G,R])
cv2.imshow("Original", original)
cv2.imshow("Ellipse Mask", mask)

bitwise_and = cv2.bitwise_and(original,original,mask)
cv2.imshow("Bitwise And",bitwise_and)






cv2.waitKey(0)
cv2.destroyAllWindows()
