import cv2


def find_contours(image):
    cv2.imshow("a", image)
    cv2.waitKey(0)
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    cv2.imshow('Contours', image)
    cv2.waitKey(0)
