import cv2
import imutils

image = cv2.imread('src/fanta_bottle.png')
template = cv2.imread('src/fanta_template.png')
cv2.imshow("Image", image)
cv2.imshow("Template", template)

image = imutils.rotate(image,30)

# convert both the image and template to grayscale
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# perform template matching
result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

print (f"{minVal}, {maxVal}, {minLoc}, {maxLoc}")

# determine the starting and ending (x, y)-coordinates of the bounding box
(startX, startY) = minLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

# draw the bounding box on the image
cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)

# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)