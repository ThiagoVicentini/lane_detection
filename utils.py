import cv2


def show_image(image, name="Image"):
    """
    Shows an image
    :param image: Image to show
    :param name: Image name
    :return: None
    """
    print(f"Showing {name}, press any key to close")
    cv2.imshow(name, image)
    cv2.waitKey()
