"""
Author: Daniel Lopez
Info from: Murtaza's Work - Robotics and AI
--> https://youtu.be/WQeoO7MI0Bs?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5
"""

import cv2
from path_helps import get_path


def main():
    my_img = "pexels_sharing.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)

    image = cv2.imread(file_path)

    # Obtain edges of the image
    # Canny params: 1)image, Threshold_1, Threshold_2.
    imgEdge = cv2.Canny(image, 100, 200)

    cv2.imshow("Edges", imgEdge)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
