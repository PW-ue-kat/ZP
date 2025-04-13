import cv2
import numpy as np

image_k = cv2.imread("src/karolak2.jpg")

(h, w, c) = image_k.shape[:3]

#Podaj StartX:300
#Podaj EndX:400
#Podaj StartY:50
#Podaj EndY:200

startX = 300
endX = 400
startY = 50
endY = 200

roi_selected = image_k[startY:endY, startX:endX]
cv2.imshow("ROI_selected", roi_selected)
cv2.waitKey(0)
cv2.destroyAllWindows()




