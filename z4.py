import cv2
import imutils

image = cv2.imread('src/fanta_bottle.png')
template = cv2.imread('src/fanta_template.png')
cv2.imshow("Image", image)
cv2.imshow("Template", template)

# convert both the image and template to grayscale
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

methods = [
    ("cv2.TM_CCOEFF",cv2.TM_CCOEFF),
    ("cv2.TM_CCOEFF_NORMED",cv2.TM_CCOEFF_NORMED),
    ("cv2.TM_CCORR",cv2.TM_CCORR),
    ("cv2.TM_CCORR_NORMED", cv2.TM_CCORR_NORMED),
    ("cv2.TM_SQDIFF",cv2.TM_SQDIFF),
    ("cv2.TM_SQDIFF_NORMED",cv2.TM_SQDIFF_NORMED)]

(h, w) = image.shape[:2]

for (name, method) in methods:
    # perform template matching
    result = cv2.matchTemplate(imageGray, templateGray, method=method)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    result_image = image.copy()
    print(f"{name}:{minVal}, {maxVal}, {minLoc}, {maxLoc}")

    # determine the starting and ending (x, y)-coordinates of the bounding box
    (startX, startY) = maxLoc
    endX = startX + template.shape[1]
    endY = startY + template.shape[0]

    # draw the bounding box on the image
    cv2.rectangle(result_image, (startX, startY), (endX, endY), (255, 0, 0), 3)

    # show the output image
    cv2.imshow(f"{name}", result_image)
    cv2.waitKey(0)