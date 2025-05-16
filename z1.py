import cv2
image = cv2.imread('src/kojot.jpg')
(h, w) = image.shape[:2]
print(f"height: {h}, width: {w}")
cv2.imshow("Original", image)

(b, g, r) = image[10, 10]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.waitKey(0)  # Czeka na dowolny klawisz, by zamknąć okno
cv2.destroyAllWindows()  # Zamknięcie wszystkich okien