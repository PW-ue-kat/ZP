# import the necessary packages
import cv2
# load the original input image and display it to our screen

poprawny_wybor = {1, 0, -1}

print("Sposób odbicia:")
print("0 – pionowe")
print("1 – poziome")
print("-1 – oba")

decyzja = int(input("Wybór użytkownika: "))

if(decyzja in poprawny_wybor):
    image = cv2.imread("src/kojot.jpg")
    flipped = cv2.flip(image, decyzja)
    cv2.imshow("Original", image)
    cv2.imshow("Flipped", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print(f"Niepoprawny wybór: '{decyzja}'")


