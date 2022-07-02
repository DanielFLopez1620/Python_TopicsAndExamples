"""
Author: Murtaza's Work - Robotics and AI
--> https://youtu.be/WQeoO7MI0Bs?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5

Modified and commented by: Daniel Lopez
"""

import cv2
from path_helps import get_path


def main():
    # Parameters for camera and cascade
    width = 640
    height = 480
    area = 0
    color = (0, 0, 255)
    cascade_xml = "haarcascade_russian_plate_number.xml"
    folder = "resources"
    cascade_path = get_path(cascade_xml, folder)
    numPlateCascade = cv2.CascadeClassifier(cascade_path)

    # Select default webcam and configure input
    video = cv2.VideoCapture(0)
    video.set(4, height)
    video.set(3, width)
    video.set(10, 100)

    # Loop to run the video
    while True:
        # Convert and read sequence
        success, fotogram = video.read()

        # Preprocess image
        imgGray = cv2.cvtColor(fotogram, cv2.COLOR_BGR2GRAY)

        # Use the cascade
        facesDetected = numPlateCascade.detectMultiScale(imgGray, 1.1, 4)

        # Define and add bounding boxes
        for (x, y, h, w) in facesDetected:
            area = w * h
            if area > 500:
                cv2.rectangle(fotogram, (x, y), (x + w, y + h), 
                              (255, 255, 0), 3)
                cv2.putText(
                    fotogram,
                    "Plate detected",
                    (x, y - 5),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    1,
                    color,
                    2,
                )
                imgCrop = fotogram[y: y + h, x: x + w]
                cv2.imshow("Detected", imgCrop)

        # Option to stop the reproduction
        cv2.imshow("Detect_Plate", fotogram)
        if cv2.waitKey(1) and 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
