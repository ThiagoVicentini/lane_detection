import cv2
import numpy as np
from sklearn.cluster import KMeans


def find_lanes(contours, image):
    """
    Find lanes in a given set of contours
    :param contours: List of contours
    :param image: Original image
    :return: Center road, New image
    """
    new_image = np.zeros(image.shape)
    center_x_coord = int(image.shape[0]/2)
    center_y_coord = int(image.shape[1]/2)

    # Compile all points in a single vector.
    points = []
    for contour in contours:
        for vector in contour:
            for point in vector:
                point_copy = point
                point_copy = np.append(point_copy, abs(point[0] - center_x_coord))
                point_copy = np.append(point_copy, np.arctan2(point[1], abs(point[0] - center_x_coord))*180/np.pi)
                points.append(point_copy)
    points = np.array(points)

    km = KMeans(n_clusters = 2, init='k-means++', n_init=200, max_iter=400, tol=1e-04)
    y = km.fit_predict(points[:, 1:2]).astype(np.int)

    road1 = points[y == 0]
    road2 = points[y == 1]
    
    for point in road1:
        cv2.circle(new_image, (int(point[0]), int(point[1])), radius=0, color=(0, 0, 255), thickness=-1)

    for point in road2:
        cv2.circle(new_image, (int(point[0]), int(point[1])), radius=0, color=(255, 0, 0), thickness=-1)

    road1_average = np.average(road1[:, 1])
    road2_average = np.average(road2[:, 1])
    if abs(road1_average - center_y_coord) < abs(road2_average - center_y_coord):
        center_road = road1
    else:
        center_road = road2
    
    return center_road, new_image
    

def find_lane_middlepoint(center_road, image):
    """
    Retuns line corresponding to the middle of the lane
    :return:
    """
    new_image = np.array(image)
    center_x_coord = int(image.shape[0]/2)

    max_negative_x = -np.inf
    max_negative_y = 0
    max_positive_x = np.inf
    max_positive_y = 0
    for point in center_road:
        if (point[0] - center_x_coord) > max_negative_x:
            max_negative_x = point[0]
            max_negative_y = point[1]
        if (point[0] - center_x_coord) < max_positive_x:
            max_positive_x = point[0]
            max_positive_y = point[1]
    
    x = (max_negative_x + max_positive_x)/2
    y = (max_negative_y + max_positive_y)/2

    cv2.circle(new_image, (int(x), int(y)), radius=0, color=(0, 255, 0), thickness=5)

    return [x, y], new_image
