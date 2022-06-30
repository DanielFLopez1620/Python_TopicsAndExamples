"""
Author: Daniel Lopez
Info from: Murtaza's Work - Robotics and AI
--> https://youtu.be/WQeoO7MI0Bs?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5
"""

import cv2
from path_helps import get_path


def main():
    # Obtain path of image
    my_video = "pexels_together.mp4"
    folder = "resources"
    file_path = get_path(my_video, folder)

    # Convert video to an object
    video = cv2.VideoCapture(file_path)

    # Loop for the video (images)
    while True:
        # Convert and read sequence
        success, fotogram = video.read()
        cv2.imshow("Video_Example", fotogram)

        # Option to stop the reproduction
        if cv2.waitKey(1) and 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
