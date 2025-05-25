# import the necessary packages
import cv2
# load the original input image and display it to our screen
image = cv2.imread("src/kojot.jpg")
cv2.imshow("Original", image)
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped around X axis (w pionie)", flipped)
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped around Y axis (w poziomie)", flipped)
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped around both axis", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()