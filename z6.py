import cv2
image = cv2.imread('src/grinch.jpg')

blue = (255,0,0)
red = (0,0, 255)
green = (0, 255,0)
white = (255, 255, 255)

(h, w) = image.shape[:2]

cY = (h//2)
cX = (w//2)



#d. Niebieskim okręgiem obejmij dookoła twarz osoby.


print(f"Sizing({h}, {w}), center {cY} {cX}")
cv2.imshow("Original", image)
#b. Czerwonymi kołami “zasłoń” osobie na zdjęciu oczy.
cv2.circle(image,(206,370),30, red,-1)
cv2.circle(image,(266,370),30, red,-1)
#c. Zielonym (białym) prostokątem “zasłoń” osobie na zdjęciu usta.
cv2.rectangle(image,(176,450),(300,500),green,-1)
#d. Niebieskim okręgiem obejmij dookoła twarz osoby.
cv2.circle(image,(cX,cY+20),180, blue,2)
cv2.imshow("Changed", image)

cv2.waitKey(0)