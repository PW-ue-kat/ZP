import cv2
# Wczytanie obrazu z pliku

def wczytaj_obraz(sciezka):
    image = cv2.imread(sciezka)
    # Sprawdzenie, czy obraz został poprawnie wczytany
    if image is None:
        print("Błąd: nie można wczytać obrazu!")
    else:
        print("Obraz wczytano poprawnie.")
        cv2.imshow("Bull", image)  # Tworzy okno i wyświetla obraz
        cv2.waitKey(0)  # Czeka na dowolny klawisz, by zamknąć okno
        cv2.destroyAllWindows()  # Zamknięcie wszystkich okien


wczytaj_obraz("src/bull.jpg")
wczytaj_obraz("src/bull2.jpg")


