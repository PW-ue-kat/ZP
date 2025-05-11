# import the necessary packages
import numpy as np
import cv2

original = cv2.imread("src/hokej.jpg")

(B, G, R) = cv2.split(original)

mask = np.zeros(original.shape[:2], dtype="uint8")

B = cv2.add(50, B)

merged = cv2.merge([B,G,R])
cv2.imshow("Original", original)
cv2.imshow("Strengthened Blue", merged)






cv2.waitKey(0)
cv2.destroyAllWindows()
