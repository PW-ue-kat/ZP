# import the necessary packages

import cv2
import imutils

mode_names = {
    cv2.RETR_TREE: 'RETR_TREE',
    cv2.RETR_EXTERNAL: 'RETR_EXTERNAL',
    cv2.RETR_LIST: 'RETR_LIST'
}

image = cv2.imread('src/kostka.png')
print(image.shape)
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
image_tmp1=image.copy()

cv2.imshow("Original", image)
cv2.imshow("Copy", image_tmp1)



thresh = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)[1]
grey = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)

images = {}

for mode in [cv2.RETR_TREE, cv2.RETR_EXTERNAL, cv2.RETR_LIST]:
    cnts = cv2.findContours(grey.copy(), mode, cv2.CHAIN_APPROX_NONE)
    cnts = imutils.grab_contours(cnts)

    image_tmp=image.copy()

    # loop over the contours
    for i, c in enumerate(cnts):
        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the image
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(image_tmp, [c], -1, (0, 0, 255), 2)
    # show the output image
    mode_name=mode_names.get(mode, 'UNKNOWN_MODE')

    cv2.imshow(f"{mode_name}", image_tmp)

#RETR_EXTERNAL nie oznacza punktu wewnatrz kostki, jedynie krawędzie

cv2.waitKey(0)



