# import the necessary packages

import cv2
import imutils
import numpy as np



image = cv2.imread('src/kostka2.png')
print(image.shape)
#Im wyższa rozdzielczość tym lepsza jakość
new_width=int(image.shape[1]*0.8)
resized = imutils.resize(image, width=new_width)
print(resized.shape)
ratio = image.shape[0] / float(resized.shape[0])

thresh = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)[1]
grey = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)

cnts = cv2.findContours(grey.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = imutils.grab_contours(cnts)


# loop over the contours
for i, c in enumerate(cnts):
    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    x, y, w, h = cv2.boundingRect(c)
    print(f"{x},{y},{w},{h}")
    (mid_x , mid_y)=(int(x+(w/2)),int(y+(h/2)))

    print(f"middle: {mid_x},{mid_y}")
    mask = np.zeros(image.shape[:2], dtype="uint8") # Create mask where white
    cv2.drawContours(mask, [c], -1, 255, -1) # Draw filled contour in mask

    segmented_brick = cv2.bitwise_and(image, image, mask=mask)
    roi = segmented_brick[y:y + h, x:x + w]


    cv2.rectangle(image,(x,y),((x+w),(y+h)),color = (0, 255, 0),thickness=2)
    cv2.putText(image,f"{w}x{h}",(x,mid_y),cv2.FONT_HERSHEY_SIMPLEX,fontScale = 1, color = (0, 255, 0),thickness=2)
    # show the output image

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


