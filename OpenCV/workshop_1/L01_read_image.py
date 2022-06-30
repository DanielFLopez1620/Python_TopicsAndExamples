"""
Author: Daniel Lopez
Info from: Murtaza's Work - Robotics and AI
--> https://youtu.be/WQeoO7MI0Bs?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5
"""

import cv2
from path_helps import get_path


def main():
    # Obtain path of the image
    my_img = "pexels_sharing.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)

    # Read image with cv2
    image = cv2.imread(file_path)

    # Display image
    cv2.imshow("Image_Example", image)

    # Generate a delay: (0) is infinite or specify a time in ms
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
