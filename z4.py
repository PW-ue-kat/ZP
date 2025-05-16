import cv2
image = cv2.imread('src/kojot.jpg')
(h, w) = image.shape[:2]
print(f"height: {h}, width: {w}")


height = int(input("Enter height pixel cord to change: "))
width = int(input("Enter width pixel cord to change: "))

if (height <h and width<w):
    cv2.imshow("Original", image)
    image[height,width] = (0, 0, 0)
    cv2.imshow("Change", image)
    cv2.waitKey(0)  # Czeka na dowolny klawisz, by zamknąć okno
    cv2.destroyAllWindows()  # Zamknięcie wszystkich okien
else:
    print(f"given height {height} should be lower than {h}, given height {width} should be lower than {w}")



