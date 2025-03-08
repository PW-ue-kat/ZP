import cv2

image_bull = cv2.imread("src/bull.jpg")
image_bull_grey = cv2.imread("src/bull_grey.jpg")


cv2.namedWindow("Bull", cv2.WINDOW_NORMAL)
cv2.imshow("Bull", image_bull)  # Tworzy okno i wyświetla obraz
cv2.waitKey(0)  # Czeka na dowolny klawisz, by zamknąć okno
cv2.destroyAllWindows()  # Zamknięcie wszystkich okien
