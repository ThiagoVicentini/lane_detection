import imageio
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.colors as mpcolors
from helper import convert_RGB_to_gray, median_filter, differential_filter

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
                    if (image[x, y][i] < filter["min"][i] or image[i] > filter["max"][i]):
                        continue
                new_image[x, y] = 1

    return new_image

def getWarpPerspective(image):
    imgSize = image.shape
    perspective = cv2.getPerspective(src, dst)
    return cv2.warpPerspective(image, perspective, imgSize)

def gaussianFilter(image):
    return cv2.GaussianBlur(image, (5, 5), 0) # Atualizar tamanho do kernel se necessário

def closing(image):
    kernel = np.ones([5, 5], np.uint8)      # Atualizar tamanho do kernel se necessário
    dilated = cv2.dilate(image, kernel)
    return cv2.erode(dilated, np.ones((5, 5), np.uint8))

def binarizeHSVImage(image, threshold):
    return cv2.inRange(image, (threshold["min"][0], threshold["min"][1], threshold["min"][2]), 
                              (threshold["max"][0], threshold["max"][1], threshold["max"][2]))


def getContours(image):
    canny_edges = cv2.Canny(image, 100, 200)
    processed = closing(canny_edges)
    contours, hierarchy = cv2.findContours(processed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def find_middlepoint(contours):
    pass

# Utilizar seed para gerar mask
# Carregar a imagem
# Aplicar wrap perspective - pulamos isso!
# Aplicar um filtro gaussiano
# Transformar a imagem no espectro HSV
# Mask
# Closing
# Encontrar os contornos (filtro diferencial)
# Pegar o centro dos contornos
# Estimar a reta (interp linear?)
# Coletar o ponto médio

if __name__ == "__main__":
    if debug:
        image = imageio.imread(image_test_path)
        denoisedImage = gaussianFilter(image)
        hsvImage = mpcolors.rgb_to_hsv(denoisedImage)
        binaryImage = binarizeHSVImage(hsvImage, hsv_filters[0])
        contours = getContours(binaryImage)
        print(contours)
        testeImage = image
        for contour in contours:
            testeImage[contour] = 255
        middleReference = find_middlepoint(contours)
        
        plt.imshow(image)
        plt.subplot(121)
        plt.imshow(binaryImage)
        plt.subplot(122)
        plt.show()
    else:
        seed = imageio.imread(seed_path)
