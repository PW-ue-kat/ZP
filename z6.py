import cv2
image = cv2.imread('src/kojot.jpg')
(h, w) = image.shape[:2]
print(f"height: {h}, width: {w}")


(cX, cY) = (w // 2, h // 2)

cv2.imshow("Original", image)

image[cY-50:cY+50, cX-50:cX+50] = (0, 0, 255)
cv2.imshow("Changed", image)
cv2.waitKey(0)  # Czeka na dowolny klawisz, by zamknąć okno
cv2.destroyAllWindows()  # Zamknięcie wszystkich okien