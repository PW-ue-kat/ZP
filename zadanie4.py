import cv2
import numpy as np

image_w = cv2.imread("src/wywern.jpg")

b, g, r = cv2.split(image_w)
M = np.ones(b.shape, dtype="uint8")*10
b = cv2.add(b, M)
M = np.ones(g.shape, dtype="uint8")*20
g= cv2.subtract(g, M)
M = np.ones(r.shape, dtype="uint8")*30
r= cv2.add(r, M)

filtered_image = cv2.merge([b, g, r])

cv2.imshow("Original", image_w)
cv2.imshow("Filtred Image", filtered_image)
cv2.imwrite("src/wywern_filtered.jpg",filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


