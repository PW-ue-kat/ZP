import cv2
image = cv2.imread('src/kojot.jpg')
(h, w) = image.shape[:2]
print(f"height: {h}, width: {w}")

pixel1 = image[50,50]
pixel2 = image[200,200]

(b1,g1,r1) = pixel1
print(f"Pixel at (50, 50) - Red: {r1}, Green: {g1}, Blue: {b1}")
(b2,g2,r2) = pixel2
print(f"Pixel at (200, 200) - Red: {r2}, Green: {g2}, Blue: {b2}")
#print(f"Pixel diff - Red: {(r2-r1)}, Green: {(g2-g1)}, Blue: {(b2-b1)}")
pixel_diff = pixel2 - pixel1
(b3,g3,r3) = pixel_diff
print(f"Pixel diff - Red: {r3}, Green: {g3}, Blue: {b3}")

pixel_diff = image[200,200] - image[50,50]
(b3,g3,r3) = pixel_diff
print(f"Pixel diff - Red: {r3}, Green: {g3}, Blue: {b3}")