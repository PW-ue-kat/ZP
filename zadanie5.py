# import the necessary packages
import numpy as np
import cv2

original = cv2.imread("src/hokej.jpg")


mask = np.zeros(original.shape[:2], dtype="uint8")
#cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)

B, G, R = cv2.split(original)

cv2.ellipse(mask,
           center=(1400, 1800),
           axes=(300, 500),
           angle=0,
           startAngle=0,
           endAngle=360,
           color=255,
           thickness=-1)


R = np.where(mask == 255, cv2.add(R, 50), R).astype(np.uint8)


cv2.imshow("Original", original)
cv2.imshow("Ellipse Mask", mask)

result = cv2.merge([B, G, R])

bitwise_and = cv2.bitwise_and(original,original,mask)
cv2.imshow("Result",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
