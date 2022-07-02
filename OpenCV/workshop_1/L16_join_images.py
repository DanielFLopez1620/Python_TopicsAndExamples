"""
Author: Daniel Lopez
Info from: Murtaza's Work - Robotics and AI
--> https://youtu.be/WQeoO7MI0Bs?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5
"""

import cv2
import numpy as np
from path_helps import get_path
from joining_images import stackImages


def main():
    # Obtain path of the image
    my_img = "pexels_cards.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)

    # Read image with cv2
    image = cv2.imread(file_path)
    print(image.shape)
    width, height = 255, 350

    # Making vertical and horizontal images
    joinHor = np.hstack((image, image))
    joinVer = np.vstack((image, image))

    # Using the stack images function
    stacked = stackImages(0.4, ([image, image, image]))

    # Display image
    cv2.imshow("Horizontal", joinHor)
    cv2.imshow("Vertical", joinVer)
    cv2.imshow("Stacked", stacked)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
