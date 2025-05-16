import cv2
image = cv2.imread('src/kojot.jpg')
(h, w) = image.shape[:2]
print(f"height: {h}, width: {w}")
cv2.imshow("Original", image)

(b, g, r) = image[(h-1), (w-1)]
print(f"Pixel at ({(h-1)}, {(w-1)}) - Red: {r}, Green: {g}, Blue: {b}")
image[(h-1), (w-1)] = (0, 0, 255)
(b, g, r) = image[(h-1), (w-1)]
print(f"Pixel at ({(h-1)}, {(w-1)}) - Red: {r}, Green: {g}, Blue: {b}")
cv2.imshow("Changed", image)





cv2.waitKey(0)  # Czeka na dowolny klawisz, by zamknąć okno
cv2.destroyAllWindows()  # Zamknięcie wszystkich okien