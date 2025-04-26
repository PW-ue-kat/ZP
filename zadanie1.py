# import the necessary packages
import numpy as np
import cv2


# draw a rectangle
# Create a black image
triangle = np.zeros((300, 300), np.uint8)

# Define three points for the triangle
pts = np.array([[150, 50] , [250, 250], [50, 250]], np.int32)
pts = pts.reshape((-1, 1, 2))


# Method 2: Filled triangle
cv2.fillPoly(triangle, [pts], color=255)

cv2.imshow('Triangle', triangle)


# draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 170), 50, 255, -1)
cv2.imshow("Circle", circle)


bitwiseAnd = cv2.bitwise_and(triangle, circle)
cv2.imshow("AND", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(triangle, circle)
cv2.imshow("OR", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(triangle, circle)
cv2.imshow("XOR", bitwiseXor)

bitwiseNot = cv2.bitwise_not(triangle)
cv2.imshow("NOT", bitwiseNot)

# Inna pozycja trójkata

# draw a rectangle
# Create a black image
triangle = np.zeros((300, 300), np.uint8)

# Define three points for the triangle
pts = np.array([[50, 50] , [250, 250], [100, 250]], np.int32)
pts = pts.reshape((-1, 1, 2))


# Method 2: Filled triangle
cv2.fillPoly(triangle, [pts], color=255)

cv2.imshow('Triangle2', triangle)



bitwiseAnd = cv2.bitwise_and(triangle, circle)
cv2.imshow("AND2", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(triangle, circle)
cv2.imshow("OR2", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(triangle, circle)
cv2.imshow("XOR2", bitwiseXor)

bitwiseNot = cv2.bitwise_not(triangle)
cv2.imshow("NOT2", bitwiseNot)



cv2.waitKey(0)
cv2.destroyAllWindows()