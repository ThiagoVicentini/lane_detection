import numpy as np
import cv2

def convert_RGB_to_gray(image, red_weight=0.07, green_weight=0.72, blue_weight=0.21):
    grayScaleImage = red_weight*image[:,:,2] + green_weight*image[:,:,1] + blue_weight*image[:,:,0]
    grayScaleImage = grayScaleImage.astype(np.uint8)
    return grayScaleImage


def median_filter(initial_image, filter_size):
    N, M = initial_image.shape
    a = (filter_size - 1) // 2

    padding = (a, a)
    padded_image = np.pad(initial_image, (padding, padding), 'constant')
    output_image = np.zeros(initial_image.shape)

    for x in range(a, N+a):
        for y in range(a, M+a):
            sub_f = padded_image[x-a: x+a+1, y-a: y+a+1]
            window_sorted = np.sort(sub_f, axis=None)
            output_image[x-a][y-a] = window_sorted[len(window_sorted)//2]

    return output_image


def differential_filter(image):
    w = np.matrix([[ 0, -1,  0], 
                   [-1,  4, -1], 
                   [ 0, -1,  0]])

    # apply convolution of the image with the differential filter
    N, M = image.shape
    n, m = w.shape
    
    a = int((n-1)/2)
    b = int((m-1)/2)

    w_flip = np.flip( np.flip(w, 0) , 1)
    g = np.array(image, copy=True)

    for x in range(a,N-a):
        for y in range(b,M-b):
            sub_f = image[ x-a : x+a+1 , y-b:y+b+1 ]
            g[x,y] = np.sum( np.multiply(sub_f, w_flip)).astype(np.uint8)

    return g


def show_image(mat):
    cv2.imshow("a", mat)
    cv2.waitKey()
