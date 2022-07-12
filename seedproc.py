import cv2
import json
import numpy as np
import imageio

from main import masks_filename


# Global variables used in trackbars
image = None
image_hsv = None

lower_mask = []
upper_mask = []


def remove_mask(masks):
    try:
        idx = int(input(f"What mask do you want to remove? (1 - {len(masks) + 1}\n").strip())
        removed_mask = masks.pop(idx - 1)
        ans = input(f"Removed mask {removed_mask}\nSave changes? [y/n]").strip()
        if ans.lower() == "y":
            with open(masks_filename, "w") as masks_file:
                json.dump(masks, masks_file)
                print("Masks file successfully updated")
        else:
            print("Ending")
            return
    except:
        print("Invalid input")


def on_trackbar(val):
    global image, image_hsv, lower_mask, upper_mask
    hue_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackedBars")

    lower_mask = np.array([hue_min, sat_min, val_min])
    upper_mask = np.array([hue_max, sat_max, val_max])

    masked_image = cv2.inRange(image, lower_mask, upper_mask)

    cv2.imshow("Original image", image)
    cv2.imshow("HSV image", image_hsv)
    cv2.imshow("Masked image", masked_image)


def update_mask(img, img_hsv, masks):
    global image, image_hsv, lower_mask, upper_mask
    image = img
    image_hsv = img_hsv
    cv2.namedWindow("TrackedBars")
    cv2.resizeWindow("TrackedBars", 640, 240)

    cv2.createTrackbar("Hue Min", "TrackedBars", 0, 179, on_trackbar)
    cv2.createTrackbar("Hue Max", "TrackedBars", 179, 179, on_trackbar)
    cv2.createTrackbar("Sat Min", "TrackedBars", 0, 255, on_trackbar)
    cv2.createTrackbar("Sat Max", "TrackedBars", 255, 255, on_trackbar)
    cv2.createTrackbar("Val Min", "TrackedBars", 0, 255, on_trackbar)
    cv2.createTrackbar("Val Max", "TrackedBars", 255, 255, on_trackbar)

    # Show some stuff
    on_trackbar(0)
    # Wait until user press some key
    cv2.waitKey()

    print("Generated mask:")
    print(lower_mask, upper_mask)

    ans = input("Do you want to insert this mask into mask file? [y/n]\n").strip()
    if ans.lower() == "y":
        masks.append({"min": lower_mask.tolist(), "max": upper_mask.tolist()})
        with open("mask.json", "w") as masks_file:
            json.dump(masks, masks_file)
            print("Mask successfully added")

    print("Ending")


def check_mask(image):
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    with open("mask.json") as mask_file:
        masks = json.load(mask_file)
        print("******* SEED PROCESSING *******")
        print(f"- Found {len(masks)} mask(s)\n")

        masked_images = []
        for idx, mask in enumerate(masks):
            min_range = np.array(mask["min"])
            max_range = np.array(mask["max"])
            masked_images.append(cv2.inRange(image_hsv, min_range, max_range))
            print(f"Mask {idx + 1}")
            print(f"{mask}\n")

        masked_image = np.sum(masked_images, axis=0) / len(masked_images)
        masked_image[masked_image != 0] = 255
        print("Opening filtered image")
        print("Press any key to close")
        cv2.imshow("Original image", image)
        cv2.imshow("Masked image", masked_image)
        cv2.waitKey()

        ans = input("Do you want to update this mask? [y/n]\n").strip()
        if ans.lower() == "y":
            update_mask(image, image_hsv, masks)
            return

        ans = input("Do you want to remove any mask? [y/n]").strip()
        if ans.lower() == "y":
            remove_mask(masks)
            return

        print("Finished")
