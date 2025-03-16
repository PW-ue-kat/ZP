import cv2
import numpy as np

image_m = cv2.imread("src/morgoth.jpg")



cv2.namedWindow("Morgoth original")
cv2.imshow("Morgoth original", image_m)


# shift the image 25 pixels to the right and 50 pixels down
M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted = cv2.warpAffine(image_m, M, (image_m.shape[1], image_m.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()