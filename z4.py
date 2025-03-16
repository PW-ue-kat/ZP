import cv2
image = cv2.imread('src/kojot.jpg')

print("Podaj współrzedne pixela do zmiany:")
a, b = map(int, input().split())

(h, w) = image.shape[:2]

if (a > (h-1)):
    print(f"nieporawna wartość X - {a}, maksymalna możliwa to {h}")
elif (b > (w-1)):
    print(f"nieporawna wartość Y - {b}, maksymalna możliwa to {w}")
else:
    image[a, b] = (0, 0, 0)
    cv2.imshow("Changed", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

