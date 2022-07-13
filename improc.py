import cv2
import json
import numpy as np

import helper
from main import masks_filename


def crop_image(image, cutting_point=2):
    """
    Returns bottom half of the image
    Assuming the camera is vertically centered, everything above the middle
    of the image probably correspond to useless information when related to lane detection
    :param image: Input image
    :param cutting_point: Point to start cutting relative to image size (2: half)
    :return: Cropped image
    """
    height = image.shape[0]
    return image[height // cutting_point: height, :, :]


def mask_image(image):
    """
    Applies binary masking specified in mask file to image
    :param image: Input image
    :return: Binary masked image
    """
    masked_images = []
    with open(masks_filename) as masks_file:
        # Load masks dictionary
        masks = json.load(masks_file)
        for mask in masks:
            # Apply each mask individually
            min_range = np.array(mask["min"])
            max_range = np.array(mask["max"])
            masked_images.append(cv2.inRange(image, min_range, max_range))

    # Merge all masks into a single one
    masked_image = np.sum(masked_images, axis=0) / len(masked_images)
    masked_image[masked_image != 0] = 255
    return np.uint8(masked_image)


def closing(image, kernel_size=None):
    """
    Performs closing morphological operation in image
    Default kernel size is [5, 5]
    :param image: Input image
    :param kernel_size: List specifying kernel size
    :return: Morphologically transformed image
    """
    # Default mutable argument
    if kernel_size is None:
        kernel_size = [5, 5]
    kernel = np.ones(kernel_size, np.uint8)
    dilated = cv2.dilate(image, kernel)
    return cv2.erode(dilated, kernel)


def detect_edges(image, tresh_lower=50, tresh_upper=150):
    """
    Perform a series of operations in an input image to detect its edges
    Image Cropping -> HSV Transform -> Gaussian Blur -> Binary Masking ->
    -> Closing -> Canny Edge Detection
    :param image: Input image
    :param tresh_lower: Lower canny threshold
    :param tresh_upper: Upper canny threshold
    :return: Edged image
    """
    cropped_image = crop_image(image)
    image_hsv = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
    masked_image = mask_image(image_hsv)
    blurred_image = cv2.GaussianBlur(masked_image, (3, 3), 0)
    closed_masked_image = closing(blurred_image)
    canny_image = cv2.Canny(closed_masked_image, tresh_lower, tresh_upper)
    edged_image = closing(canny_image)
    return edged_image
