import cv2
import numpy as np

image_k = cv2.imread("src/karolak2.jpg")

(h, w, c) = image_k.shape[:3]

startX = int(input("Podaj StartX:"))
endX = int(input("Podaj EndX:"))
startY = int(input("Podaj StartY:"))
endY = int(input("Podaj EndY:"))

if (startY < h and startX < w and endY < h and endX < w):
    roi_selected = image_k[startY:endY, startX:endX]
    cv2.imshow("ROI_selected", roi_selected)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Podane wymiar poza maksymalnym zakresem Y - {h}, X - {w}")



cv2.imshow("ROI_lower",roi_right)



