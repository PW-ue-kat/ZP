import cv2
# Wczytanie obrazu z pliku
image = cv2.imread("src/bull.jpg")
# Sprawdzenie, czy obraz został poprawnie wczytany

(h, w, c) = image.shape[:3]
print(f'channels: {c}')
