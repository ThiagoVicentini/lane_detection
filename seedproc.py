import cv2
import json
import numpy as np
from main import image_path as path


# Number of different masks
n_masks = 1




"""
Open test image with sliders and prompt for user filtering
Update filter stored in file 
"""
cv2.namedWindow("TrackedBars")
cv2.resizeWindow("TrackedBars", 640, 240)


def on_trackbar(val):
    hue_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackedBars")

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    imgMASK = cv2.inRange(imgHSV, lower, upper)

    cv2.imshow("Output1", img)
    cv2.imshow("Output2", imgHSV)
    cv2.imshow("Mask", imgMASK)


img = cv2.imread(path)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.createTrackbar("Hue Min", "TrackedBars", 0, 179, on_trackbar)
cv2.createTrackbar("Hue Max", "TrackedBars", 179, 179, on_trackbar)
cv2.createTrackbar("Sat Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Sat Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("Val Min", "TrackedBars", 0, 255, on_trackbar)
cv2.createTrackbar("Val Max", "TrackedBars", 255, 255, on_trackbar)

# Show some stuff
on_trackbar(0)
# Wait until user press some key
cv2.waitKey()

