import cv2
import numpy as np
import imutils

image_m = cv2.imread("src/morgoth.jpg")

print("Podaj wartosc do przesuniecia:")
x, y = map(int, input().split())

cv2.namedWindow("Morgoth original")
cv2.imshow("Morgoth original", image_m)


shifted = imutils.translate(image_m, x, y)
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)


cv2.destroyAllWindows()