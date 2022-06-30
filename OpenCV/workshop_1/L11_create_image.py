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
    cv2.imshow("Black_Image", image)
    cv2.waitKey(0)

    # Change color using RGB
    image[:] = 255, 0, 0
    cv2.imshow("Blue_Image", image)
    cv2.waitKey(0)

    # Modifying parts of the image
    image[100:200, 300:400] = 0, 255, 255
    image[10:100, 100:299] = 255, 0, 255
    cv2.imshow("First_Collage", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
