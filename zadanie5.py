import cv2
import numpy as np

image_w = cv2.imread("src/wywern.jpg")
image_wf = cv2.imread("src/wywern_filtered.jpg")



cv2.imshow("Original", image_w)
cv2.imshow("Filtred Image", image_wf)
diff = cv2.absdiff(image_w, image_wf)
cv2.imshow("Diff", diff)



cv2.waitKey(0)
cv2.destroyAllWindows()


