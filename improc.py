import cv2
import json
import numpy as np

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
    masked_images = []
    with open(masks_filename) as masks_file:
        masks = json.load(masks_file)
        for mask in masks:
            min_range = np.array(mask["min"])
            max_range = np.array(mask["max"])
            masked_images.append(cv2.inRange(image, min_range, max_range))

    masked_image = np.sum(masked_images, axis=0) / len(masked_images)
    masked_image[masked_image != 0] = 255
    return np.uint8(masked_image)


def closing(image, kernel_size=[5, 5]):
    kernel = np.ones(kernel_size, np.uint8)  # Atualizar tamanho do kernel se necessário
    dilated = cv2.dilate(image, kernel)
    return cv2.erode(dilated, np.ones((5, 5), np.uint8))


def detect_edges(image, tresh_lower=50, tresh_upper=150):
    cropped_image = crop_image(image)
    image_hsv = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
    blurred_image = cv2.GaussianBlur(image_hsv, (5, 5), cv2.BORDER_DEFAULT)
    masked_image = mask_image(blurred_image)
    closed_masked_image = closing(masked_image)
    edged_image = cv2.Canny(closed_masked_image, tresh_lower, tresh_upper)
    return edged_image
