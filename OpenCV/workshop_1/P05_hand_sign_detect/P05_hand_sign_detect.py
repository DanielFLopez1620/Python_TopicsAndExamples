"""
Author: Murtaza's Work - Robotics and AI
--> https://youtu.be/wa2ARoUUdU8?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5
Modified and commented by: Daniel Lopez
"""

import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time
import os
import path_helps

def main():
    # Params and variables
    offset = 20
    imgSize = 300
    count = 0

    # Paths for data and info
    dataFolder = "data"
    dataSubFolder = "A"
    dataPath = path_helps.get_path_dir("OpenCV", "workshop1")
    dataPath = os.path.join(dataPath, dataFolder)
    dataPath = os.path.join(dataPath, dataSubFolder)

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

            # Generate a new image
            newImage = np.ones((imgSize, imgSize, 3), np.uint8)
            
            # Get size and ratio to figure out the needed resize form
            cropSize = cropFotogram.shape
            sizeRatio = h/w

            # Change according the height
            if sizeRatio > 1:
                changeValue = imgSize/h
                wResize = math.ceil(changeValue * w)
                imgChange = cv2.resize(cropFotogram, (wResize, imgSize))
                wCenter = math.ceil((300-wResize)/2)
                newImage[:, wCenter:wResize + wCenter] = imgChange
            # Change according the width
            elif sizeRatio < 1:
                changeValue = imgSize/h
                hResize = math.ceil(changeValue * w)
                imgChange = cv2.resize(cropFotogram, (hResize, imgSize))
                hCenter = math.ceil((300-hResize)/2)
                newImage[hCenter:hResize + hCenter,:] = imgChange   

        # Display fotogram to create a video
        cv2.imshow("Video", fotogram)
        cv2.imshow("Hand obtained", cropFotogram)
        key = cv2.waitKey(1)
        if key == ord('s'):
            count += 1
            timeName = f"Image_{time.time()}.jpg"
            handFile = os.path.join(dataPath, timeName)
            cv2.imwrite(dataPath)
            print(f"Counter: {count}")



if __name__ == "__main__":
    main()