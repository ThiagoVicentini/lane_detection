import numpy as np
import matplotlib.colors as mpcolors

"""
Convert image from RGB to HSV color spectrum
image: np.matrix - Input image
return: np.matrix - Image in HSV
"""
def convert_rgb_hsv(image: np.matrix) -> np.matrix:
    # Conversion function
    return mpcolors.rgb_to_hsv(image)


def find_canny_edges():
    pass


def dilate_borders():
    pass


def erode_borders():
    pass
