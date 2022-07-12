import imageio

import contour
import improc

seed_path = ""
image_test_path = "dataset_examples/um_000003.png"
masks_filename = "mask.json"
debug = True
generate_seed = False


if __name__ == "__main__":
    image = imageio.imread(image_test_path)
    if generate_seed:
        from seedproc import check_mask
        check_mask(image)
        quit()

    # Processes image to get lane edges
    processed_image = improc.detect_edges(image)
    contour.find_contours(processed_image)

    # Encontrar os contornos (filtro diferencial)
    # Pegar o centro dos contornos
    # Estimar a reta (interp linear?)
    # Coletar o ponto médio
