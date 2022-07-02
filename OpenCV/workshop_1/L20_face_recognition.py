"""
Author: Daniel Lopez
Info from: Murtaza's Work - Robotics and AI
--> https://youtu.be/WQeoO7MI0Bs?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5
"""

import cv2
from path_helps import get_path


def main():
    # Obtain path of the image
    my_img = "pexels_man.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)

    # Read cascade
    cascade_xml = "haarcascade_frontalface_default.xml"
    cascade_path = get_path(cascade_xml, folder)
    print(cascade_path)
    faceCascade = cv2.CascadeClassifier(cascade_path)  # Read image with cv2

    # Read image
    image = cv2.imread(file_path)
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Dectect faces (frontal)
    facesDetected = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    # Define and add bounding boxes
    for (x, y, h, w) in facesDetected:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 3)

    # Display image
    cv2.imshow("Output", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
