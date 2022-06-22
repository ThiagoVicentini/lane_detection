import numpy as np

def convert_RGB_to_gray(image, red_weight=0.07, green_weight=0.72, blue_weight=0.21):
    grayScaleImage = red_weight*image[:,:,2] + green_weight*image[:,:,1] + blue_weight*image[:,:,0]
    grayScaleImage = grayScaleImage.astype(np.uint8)
    return grayScaleImage


def median_filter(initialImage, filterSize):
    N, M = initialImage.shape
    a = (filterSize-1)//2

    padding = (a, a)
    paddedImg = np.pad(initialImage, (padding, padding), 'constant')
    outputImage = np.zeros(initialImage.shape)

    for x in range(a, N+a):
        for y in range(a, M+a):
            sub_f = paddedImg[ x-a: x+a+1, y-a: y+a+1 ]
            windowSorted = np.sort(sub_f, axis=None)
            outputImage[x-a][y-a] = windowSorted[len(windowSorted)//2]

    return outputImage

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