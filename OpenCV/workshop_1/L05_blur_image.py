"""
Author: Daniel Lopez
Info from: Murtaza's Work - Robotics and AI
--> https://youtu.be/WQeoO7MI0Bs?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5
"""

import cv2
from path_helps import get_path


def main():
    # Obtain path of image
    my_img = "pexels_sharing.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)

    # Read image
    image = cv2.imread(file_path)

    # Convert image to gray scale
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Make a blur
    # Gaussian Blur params: cv2 image , Kernel (odd numbers rectangle), Sigma.
    imgBlur = cv2.GaussianBlur(imgGray, (9, 9), 0)

    cv2.imshow("BlurImage", imgBlur)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
