import cv2
image = cv2.imread('src/kojot.jpg')

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)


(b, g, r) = image[cY, cX]
print(f"Pixel at ({cY}, {cX}) - Red: {r}, Green: {g}, Blue: {b}")

