# import the necessary packages
import numpy as np
import cv2
import random

canvas = np.zeros((400, 400, 3), dtype="uint8")

blue = (255,0,0)
red = (0,0, 255)
green = (0, 255,0)
white = (255, 255, 255)

cv2.imshow("Original", canvas)

colors = [blue,green,red,white]

# Zmodyfikuj kod pętli rysującej okręgi, aby zamiast okręgów rysowała
# kwadraty. Każdy kolejny kwadrat powinien być większy o 20 pikseli od
# poprzedniego i mieć środek w tym samym miejscu.

#Czerwony okrąg o promieniu 60 px w środku obrazu.
(h, w) = canvas.shape[:2]
cY = (h//2)
cX = (w//2)



for a in range(0, 180, 20):
    selected_color = random.choice(colors)
    cv2.rectangle(canvas,(cX-a, cY-a),(cX+a, cY+a),selected_color)

cv2.imshow("Changed", canvas)

cv2.waitKey(0)