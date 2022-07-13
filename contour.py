import cv2
import numpy as np


def find_contours(image):
    """
    Find contours in canny edged image
    :param image: Input image
    :return: Contours array and corresponding image
    """
    # Perform contour detection
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cont_image = np.zeros([image.shape[0], image.shape[1], 3])

    approximated_contours = []
    # Approximate each contour by a simpler shape
    for contour in contours:
        epsilon = 0.01 * cv2.arcLength(contour, True)
        # Approximate by a polygon and force it to be convex
        approximated_contour = cv2.approxPolyDP(contour, epsilon, True)
        convex_contour = cv2.convexHull(approximated_contour)
        approximated_contours.append(convex_contour)
        cv2.drawContours(cont_image, [convex_contour], -1, (0, 255, 0), 1)

    return contours, cont_image
