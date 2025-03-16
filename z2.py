import cv2
image = cv2.imread('src/kojot.jpg')


(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

(h, w) = image.shape[:2]
(b, g, r) = image[h-1, w-1]

print(f"Pixel at ({h}, {w}) - Red: {r}, Green: {g}, Blue: {b}")

cv2.imshow("Original", image)
image[h-1, w-1] = (0, 0, 255)
(b, g, r) = image[h-1, w-1]
print(f"Pixel at ({h}, {w}) - Red: {r}, Green: {g}, Blue: {b}")
cv2.imshow("Changed", image)
cv2.waitKey(0)