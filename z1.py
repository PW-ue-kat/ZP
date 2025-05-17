import cv2
image = cv2.imread('src/kojot.jpg')

blue = (255,0,0)

(h, w) = image.shape[:2]

cY = (h//2)
cX = (w//2)

cv2.imshow("Original", image)
cv2.line(image,(cX, cY), (w-1,h-1),blue,2)
cv2.imshow("Changed", image)

cv2.waitKey(0)