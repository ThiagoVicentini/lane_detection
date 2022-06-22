import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mpcolors
from helper import generate_image_median_filter, convert_RGB_to_gray, differential_filter

seed_path = ""
image_test_path = "dataset_examples/um_000003.png" 
debug = True

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




def find_middlepoint():
    pass


if __name__ == "__main__":
    if debug:
        image = imageio.imread(image_test_path)
        grayImage = convert_RGB_to_gray(image)
        filtered_image = generate_image_median_filter(grayImage, 5)
        filtered_image = differential_filter(filtered_image)

        fig = plt.figure()
        plt.subplot(131)
        plt.imshow(image)
        plt.subplot(132)
        plt.imshow(grayImage)
        plt.subplot(133)
        plt.imshow(filtered_image)
        plt.show()
    else:
        seed = imageio.imread(seed_path)
