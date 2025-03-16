import cv2
import numpy as np

image_m = cv2.imread("src/morgoth.jpg")



cv2.namedWindow("Morgoth original")
cv2.imshow("Morgoth original", image_m)


# now, let's shift the image 20 pixels to the left and 50 pixels
# up by specifying negative values for the x and y directions,
# respectively
M = np.float32([[1, 0, -20], [0, 1, -50]])
shifted = cv2.warpAffine(image_m, M, (image_m.shape[1], image_m.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()