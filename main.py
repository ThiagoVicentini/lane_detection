import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mpcolors

"""
Define HSV filtering interval
Array of dictionaries with mask intervals
min and max define hue interval to be considered
"""
hsv_filters = [{
    # To be set by seeding method
    "min": [0, 0, 0],
    "max": [179, 179, 255]
}]


"""
Applies mask filtering in a given image
image: np.matrix - Input image
hsv_filter: list - List containing dictionaries with HSV filtering interval
"""
def apply_mask(image: np.matrix, hsv_filters: list) -> None:
    new_image = np.zeros([image.shape[0], image.shape[1]])
    for filter in hsv_filters:
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                for i in range(3):
                    if (image[x, y][i] < filter["min"][i] or
                            image[i] > filter["max"][i]):
                        continue
                new_image[x, y] = 1

    return new_image


"""
Convert image from RGB to HSV color spectrum
image: np.matrix - Input image
return: np.matrix - Image in HSV
"""
def convert_rgb_hsv(image: np.matrix) -> np.matrix:
    # Conversion function
    return mpcolors.rgb_to_hsv(image)


if __name__ == "__main__":
    pass
