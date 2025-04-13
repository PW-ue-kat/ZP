import cv2
import numpy as np

image_k = cv2.imread("src/karolak2.jpg")

(h, w, c) = image_k.shape[:3]

selected_rois = []


for y in range(3):
    for x in range (3):
        roi_selected = image_k[y*int(h/3):(y+1)*int(h/3), x*int(w/3):(x+1)*int(w/3)]
        selected_rois.append(roi_selected)


for index, roi in enumerate(selected_rois):
    cv2.imshow(f"{index}", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()




