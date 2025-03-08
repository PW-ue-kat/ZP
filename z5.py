import cv2

image_bull = cv2.imread("src/bull.jpg")
image_bull_grey = cv2.imread("src/bull_grey.jpg")


cv2.namedWindow("Bull")
cv2.imshow("Bull", image_bull)

cv2.namedWindow("Bull Grey")
cv2.imshow("Bull Grey", image_bull_grey)

k = cv2.waitKey(0)
print(k)

while True:
    k = cv2.waitKey(0) & 0xFF
    print(k)
    if k == ord('s'): # you can put any key here
        cv2.destroyWindow("Bull Grey")
    if k == ord('k'): # you can put any key here
        cv2.destroyWindow("Bull")
    if k == ord('a'): # you can put any key here
        cv2.destroyAllWindows()
        break


