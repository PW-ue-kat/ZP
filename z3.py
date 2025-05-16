import cv2
image = cv2.imread('src/kojot.jpg')
(h, w) = image.shape[:2]
print(f"height: {h}, width: {w}")
cv2.imshow("Original", image)

mid_h = int(h/2)
mid_w = int(w/2)
print(f"mid height: {mid_h}, mid width: {mid_w}")


