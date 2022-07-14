"""
Author: Murtaza's Work - Robotics and AI
--> https://youtu.be/wa2ARoUUdU8?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5
Modified and commented by: Daniel Lopez
"""

import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
def main():
    # Params and variables
    offset = 20
    imgSize = 300

    # Capture video from webcam
    webcam = cv2.VideoCapture(0)
    handDetector = HandDetector(maxHands=1)

    while True:
        # Read fotogram from webcam
        success, fotogram = webcam.read()

        # Detect hand
        hands, fotogram = handDetector.findHands(fotogram)

        # If a hand is detected
        if hands:
            # Assign hand and get its bounding box
            hand = hands[0]
            x, y, w, h = hand["bbox"]
            
            # Crop to obtain only the hand
            cropFotogram = fotogram[y-offset:y+h-offset, x-offset:x+w-offset]

            # Generate a new image and resize the cropped fotogram
            newImage = np.ones((imgSize, imgSize, 3), np.uint8)
            cropSize = cropFotogram.shape
            newImage[0:cropSize[0], 0:cropSize[1]] = cropFotogram
            # TODO: Continue the code


        # Display fotogram to create a video
        cv2.imshow("Video", fotogram)
        cv2.imshow("Hand obtained", cropFotogram)
        cv2.waitKey(1)
