import imageio

import contour
import improc

image_test_path = "dataset_examples/um_000052.png"
masks_filename = "mask.json"
generate_seed = False


if __name__ == "__main__":
    image = imageio.imread(image_test_path)
    if generate_seed:
        from seedproc import check_mask
        check_mask(image)
        quit()

    # Processes image to get lane edges
    processed_image = improc.detect_edges(image)
    contours, cont_image = contour.find_contours(processed_image)

    # Pegar o centro dos contornos
    # Estimar a reta (interp linear?)
    # Coletar o ponto médio
