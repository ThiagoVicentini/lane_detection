# Lane Detection

Code repository for the final project of the course SCC0251 - Image Processing

## Objective

The main objective of the project is to design an algorithm that is capable of identifying road lanes in a given input image. The program must also find the midpoint of the road in order to feed a possible control algorithm for autonomous vehicles.

## Input Images

Input images will be road acquired images by real vehicles. The dataset chosed by the development team is the [KITTI-Road/Lane Detection Evaluation 2013](https://www.kaggle.com/datasets/tryingit/roadlane-detection-evaluation-2013?resource=download). It has been created in collaboration with Jannik Fritsch and Tobias Kuehnl from Honda Research Institute Europe GmbH. The main reason for that decision is the lane uniformity visually shown in the dataset, helping in the implementation tests. Some images can be seen in "Dataset" folder in this repository.

Other datasets found:
- [CurveLanes](https://github.com/SoulmateB/CurveLanes)
- [TuSimple](https://github.com/TuSimple/tusimple-benchmark)
- [Robust-Lane-Detection](https://github.com/qinnzou/Robust-Lane-Detection/blob/master/README.md)
- [CULane](https://xingangpan.github.io/projects/CULane.html)

## Step by Step

In order to achieve what has been proposed, the team is thinking about applying a mask to the input image, filtering it by a predefined color in the HSV spectrum. Said filter will give as a result an image filled with ones in places where the color is within the defined range and zeros anywhere else.

The following procedure will be to dilate and erode the image to best find the edges. 

Finally, an interpolation algorithm will be applied to estimate an extension of the lane. The midpoint can be found afterwards by taking the horizontal average of side lanes.
