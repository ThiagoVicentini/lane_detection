# Pegar o centro dos contornos
# Estimar a reta (interp linear?)
# Coletar o ponto médio

import cv2
import numpy as np

from sklearn.cluster import KMeans
from utils import show_image

def interpolation():
    pass


def find_lane_candidates():
    pass


def find_lanes(contours, image):
    new_image = np.zeros(image.shape)

    #Compile all points in a single vector.
    points = []
    for contour in contours:
        for point in contour:
            for a in point:
                points.append(a)
    points = np.array(points)

    km = KMeans(n_clusters = 2, init='k-means++', n_init=10, max_iter=300, tol=1e-04)
    y = km.fit_predict(points).astype(np.int)

    road1 = points[y==0]
    road2 = points[y==1]
    
    for point in road1:
        cv2.circle(new_image, (point[0], point[1]), radius=0, color=(0, 0, 255), thickness=-1)

    for point in road2:
        cv2.circle(new_image, (point[0], point[1]), radius=0, color=(255, 0, 0), thickness=-1)
        
    return points, new_image


def find_lane_middlepoint():
    """
    Retuns line corresponding to the middle of the lane
    :return:
    """
    pass
