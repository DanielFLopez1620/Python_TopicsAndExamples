"""
Author: Daniel Lopez
Info from: Murtaza's Work - Robotics and AI
--> https://youtu.be/WQeoO7MI0Bs?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5
"""
import cv2
import numpy as np


def main():
    # Create a new matrix (black image)
    image = np.zeros((512, 512, 3), np.uint8)

    # Insert a lines
    # params: image, start point (x,y), end point(x,y), color (BRG), thickness
    cv2.line(image, (300, 10), (200, 255), (0, 255, 0), 1)
    cv2.line(image, (50, 200), (image.shape[1], image.shape[0]),
             (255, 0, 255), 2)
    cv2.imshow("Using_Lines", image)
    cv2.waitKey(0)

    # Insert rectangles
    # params: image, start point (x,y), end point(x,y), color (BRG), thickness
    cv2.rectangle(image, (255, 200), (10, 400), (100, 0, 255), 3)
    cv2.rectangle(image, (255, 250), (400, 400), (0, 255, 0), cv2.FILLED)
    cv2.imshow("Using_Rectangles", image)
    cv2.waitKey(0)

    # Insert circles
    # params: image, center point, radius, color (RGB)
    cv2.circle(image, (400, 100), 50, (150, 150, 0), 2)
    cv2.imshow("Using_Circles", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
