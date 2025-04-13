from operator import truediv

import cv2
import numpy as np

image_k = cv2.imread("src/karolak2.jpg")

(h, w, c) = image_k.shape[:3]

selected_rois = []

selected_x =0
step=10
selection_width=100
while (selected_x+selection_width)<w:
    roi_selected = image_k[:, selected_x:selected_x+selection_width]
    cv2.imshow(f"{selected_x }",roi_selected)
    selected_x = selected_x+step
    cv2.waitKey(0)


cv2.destroyAllWindows()







