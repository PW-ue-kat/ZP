import cv2
import easyocr
import numpy as np

# Load image
image = cv2.imread('src/3.jpg')

# Preprocessing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 100, 200)

cv2.imshow("Original", image)

cv2.imshow("gray", gray)
cv2.imshow("blur", blur)
cv2.imshow("edges",edges)




# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

plate_img = None
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    aspect_ratio = w / float(h)
    if 2 < aspect_ratio < 6:  # Typical license plate aspect ratio
        plate_img = image[y:y+h, x:x+w]
        break



if plate_img is not None:
    cv2.imshow("plate_img", plate_img)

    # OCR with EasyOCR
    reader = easyocr.Reader(['en'])
    result = reader.readtext(plate_img)
    if result:
        print("Detected License Plate:", result[0][1])
    else:
        print("License plate could not be read.")
else:
    print("License plate region not found.")

cv2.waitKey(0)
cv2.destroyAllWindows()