#Extract color from picture

import numpy as np
import cv2

image = cv2.imread("src/stolik.png")

cv2.imshow("Original", image)

# Convert to HSV color space (better for color segmentation)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define color range to extract (here: orange)
lower_blue = np.array([5, 100, 100])    # HSV lower bounds
upper_blue = np.array([40, 255, 255]) # HSV upper bounds

# Create mask
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply mask to original image using bitwise AND
result = cv2.bitwise_and(image, image, mask=mask)

# Display results
cv2.imshow('Original', image)
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()