import numpy as np
import cv2

image = cv2.imread("src/stolik.png")

cv2.imshow("Original", image)


mask = np.zeros(image.shape[:2], dtype="uint8")
#cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)

cv2.ellipse(mask,
           center=(25, 100),
           axes=(40, 50),
           angle=0,
           startAngle=0,
           endAngle=360,
           color=255,
           thickness=-1)
cv2.imshow("Ellipse Mask", mask)


# apply our mask -- notice how only the person in the image is
# cropped out
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)

cv2.waitKey()
cv2.destroyAllWindows()