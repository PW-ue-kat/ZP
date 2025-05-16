import cv2
import numpy as np
image = cv2.imread('src/kojot.jpg')
(h, w) = image.shape[:2]
print(f"height: {h}, width: {w}")


def summation(test_tup):
    # Convert the tuple to a list using a list comprehension
    test = [x for x in test_tup]
    suma = np.sum(test)
    #print(suma)
    # Find the sum of the elements in the list using the built-in sum() function
    return suma
def find_brightest(image):
    brightest = (0,0,0)
    brightest_x = None
    brightest_y = None
    for y in range(0,(h-1)):
        for x in range(0, (w-1)):
            if(summation(brightest)<summation(image[y,x])):
                brightest=image[y,x]
                brightest_x = x
                brightest_y = y
            if summation(image[y,x]) == 765:
                return brightest_y, brightest_x, brightest
    return brightest_y, brightest_x, brightest

(brightest_y, brightest_x, brightest) = find_brightest(image)
(b,g,r) = brightest
print(f"Brightest pixel at {brightest_y, brightest_x}: - Red: {r}, Green: {g}, Blue: {b}")



