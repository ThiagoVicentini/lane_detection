import numpy as np
import matplotlib.colors as mpcolors
from skimage import morphology
from cv2 import Canny

"""
Convert image from RGB to HSV color spectrum
image: np.matrix - Input image
return: np.matrix - Image in HSV
"""
def convert_rgb_hsv(image: np.matrix) -> np.matrix:
    # Conversion function
    return mpcolors.rgb_to_hsv(image)


def find_canny_edges(img,t1,t2):
    return Canny(img,t1,t2)

#for binary images
def dilate_borders(img, struc_elem):
    return morphology.binary_dilation(img, struc_elem).astype(np.uint8)

#for binary images
def erode_borders(img, struc_elem):
    return morphology.binary_erosion(img,struc_elem).astype(np.uint8)    

#for binary images
def closing_borders(img, struc_elem):
    return erode_borders(dilate_borders(img,struc_elem),struc_elem)
