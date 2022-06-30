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

    # Insert text
    # params: image, text, origin(x,y), font, thickness, color, scale.
    cv2.putText(image, "Python", (160, 256), cv2.FONT_HERSHEY_COMPLEX, 2,
                (255, 0, 100), 1)

    # Display results
    cv2.imshow("Inserting_text", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
