import cv2
# Wczytanie obrazu z pliku
image_gray = cv2.imread("src/bull.jpg", cv2.IMREAD_GRAYSCALE)
# Sprawdzenie, czy obraz został poprawnie wczytany

cv2.imwrite("src/bull_grey.jpg",image_gray)