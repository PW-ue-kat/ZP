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
(roi_h, roi_w) = roi_selected.shape[:2]

x_offset, y_offset = 50, 50
image_k[y_offset:y_offset+roi_h,x_offset:x_offset+roi_w]= roi_selected


cv2.imshow("ROI_pasted", image_k)
cv2.waitKey(0)
cv2.destroyAllWindows()




