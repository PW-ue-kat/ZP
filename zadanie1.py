# import the necessary packages

import cv2
import imutils

image = cv2.imread('src/kostka.png')
print(image.shape)
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
grey = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh100 = cv2.threshold(resized, 135, 255, cv2.THRESH_BINARY)[1]
thresh140 = cv2.threshold(resized, 140, 255, cv2.THRESH_BINARY)[1]
thresh180 = cv2.threshold(resized, 145, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('thresh100', thresh100)
cv2.imshow('thresh140', thresh140)
cv2.imshow('thresh180', thresh180)
cv2.imshow('grey', grey)
cv2.waitKey(0)