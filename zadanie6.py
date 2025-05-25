# import the necessary packages
import numpy as np
import cv2

original = cv2.imread("src/OpenCV.png")


mask = np.zeros(original.shape[:2], dtype="uint8")
#cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)

B, G, R = cv2.split(original)

cv2.imshow("Original", original)

cv2.imshow("Original", original)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

result = cv2.merge([R, G, B])

cv2.imshow("Result - flipped R<>B", result)

R = np.zeros(original.shape[:2], dtype="uint8")

result = cv2.merge([B, G, R])
cv2.imshow("Cleared R", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
