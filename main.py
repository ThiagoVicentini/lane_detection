import imageio

import contour
import improc
import lane

image_test_path = "dataset_examples/um_000052.png"
masks_filename = "mask.json"
generate_seed = False
debug = False


if __name__ == "__main__":
    image = imageio.imread(image_test_path)
    if generate_seed:
        from seedproc import check_mask
        check_mask(image)
        quit()

    # Processes image to get lane edges
    processed_image = improc.detect_edges(image)
    contours, cont_image = contour.find_contours(processed_image)
    center_road, lane_image = lane.find_lanes(contours, image)
    center_point = lane.find_lane_middlepoint(center_road)

    if debug:
        from utils import show_image
        show_image(image, "Original image")
        show_image(processed_image, "Masked image")
        show_image(cont_image, "Convex contours")
        show_image(lane_image, "Lanes")
