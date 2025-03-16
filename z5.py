import cv2
image = cv2.imread('src/kojot.jpg')

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

image[0:cY, 0:cX] = (255, 0, 0)
cv2.imshow("Changed", image)
cv2.waitKey(0)
cv2.destroyAllWindows()