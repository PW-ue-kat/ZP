import cv2
# Wczytanie obrazu z pliku
image_gray = cv2.imread("src/bull.jpg", cv2.IMREAD_GRAYSCALE)
# Sprawdzenie, czy obraz został poprawnie wczytany




print(f'ndim: {image_gray.ndim}')

if image_gray.ndim == 2:

    channels = 1 #single (grayscale)
    print(f'channels: {channels}')

if image_gray.ndim == 3:
    (h, w, c) = image_gray.shape[:3]
    print(f'channels: {c}')
