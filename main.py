import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mpcolors

hsv_filter = {
    "min": [0, 0, 0],
    "max": [179, 179, 255]
}


def apply_mask(image, hsv_filter):
    new_image = np.zeros([image.shape[0], image.shape[1]])
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            for i in range(3):
                if (image[x, y][i] < hsv_filter["min"][i] or
                        image[i] > hsv_filter["max"][i]):
                    continue
            new_image[x, y] = 1

    return new_image


def convert_rgb_hsv(image):
    hsv_image = np.zeros([image.shape[0], image.shape[1]], np.uint8)
    # Conversion function
    return hsv_image


def convert_rgb_hsv_mpl(image):
    return mpcolors.rgb_to_hsv(image)


if __name__ == "__main__":
    pass
