# import the necessary packages
import numpy as np
import cv2

original = cv2.imread("src/hokej.jpg")

(B, G, R) = cv2.split(original)

mask = np.zeros(original.shape[:2], dtype="uint8")

merged = cv2.merge([R,G,B])
cv2.imshow("Changed channels", merged)



merged = cv2.merge([mask,G,R])
cv2.imshow("MergedGR", merged)

merged = cv2.merge([mask,G,mask])
cv2.imshow("MergedG", merged)


merged = cv2.merge([mask,mask,R])
cv2.imshow("MergedR", merged)


cv2.waitKey(0)
cv2.destroyAllWindows()
