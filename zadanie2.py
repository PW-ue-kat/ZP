# import the necessary packages
import numpy as np
import cv2

balrog_original = cv2.imread("src/balrog.jpg")
balrog_modified = cv2.imread("src/balrog2.jpg")


bitwiseXor = cv2.bitwise_xor(balrog_original, balrog_modified)
cv2.imshow("XOR",bitwiseXor)

cv2.waitKey()
cv2.destroyAllWindows()