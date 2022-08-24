"""
Author: Murtaza's Work - Robotics and AI
--> https://youtu.be/wa2ARoUUdU8?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5
Modified and commented by: Daniel Lopez
"""

import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import os
import tensorflow
import path_helps


def main():
    # Params and variables
    offset = 20
    imgSize = 300
    count = 0
    labels = ["F"]

    # Paths for data and info
    dataFolder = "data"
    dataSubFolder = "A"
    modelFolder = "model"
    modelClassifier = "keras_model.h5"
    modelTxt = "labels.txt"
    dataPath = modelPath = path_helps.get_path_dir(dataFolder, dataSubFolder)
    # modelPath = modelPathTxt = path_helps.get_path_dir(modelFolder)
    modelPath = path_helps.get_path(modelClassifier, modelPath)
    modelPathTxt = path_helps.get_path(modelTxt, modelFolder)
    # Capture video from webcam
    webcam = cv2.VideoCapture(0)

    # Create detector and classifier:
    handDetector = HandDetector(maxHands=1)
    classifyHand = Classifier(modelPath, modelPathTxt)

    while True:
        # Read fotogram from webcam
        success, fotogram = webcam.read()
        imgResult = fotogram.copy()
        # Detect hand
        hands, fotogram = handDetector.findHands(fotogram)

        # If a hand is detected
        if hands:
            # Assign hand and get its bounding box
            hand = hands[0]
            x, y, w, h = hand["bbox"]

            # Crop to obtain only the hand
            cropFotogram = fotogram[
                y - offset: y + h - offset, x - offset: x + w - offset
            ]

            # Generate a new image
            newImage = np.ones((imgSize, imgSize, 3), np.uint8)

            # Get size and ratio to figure out the needed resize form
            cropSize = cropFotogram.shape
            sizeRatio = h / w

            # Change according the height
            if sizeRatio > 1:
                changeValue = imgSize / h
                wResize = math.ceil(changeValue * w)
                imgChange = cv2.resize(cropFotogram, (wResize, imgSize))
                wCenter = math.ceil((300 - wResize) / 2)
                newImage[:, wCenter: wResize + wCenter] = imgChange
                predict, ind = classifyHand.getPrediction(newImage, draw=False)
            # Change according the width
            elif sizeRatio < 1:
                changeValue = imgSize / h
                hResize = math.ceil(changeValue * w)
                imgChange = cv2.resize(cropFotogram, (hResize, imgSize))
                hCenter = math.ceil((300 - hResize) / 2)
                newImage[hCenter: hResize + hCenter, :] = imgChange
                predict, ind = classifyHand.getPrediction(newImage, draw=False)

        # Add the result of the classification
        cv2.putText(
            imgResult,
            labels[ind],
            (x, y - 15),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (255, 0, 255),
        )
        cv2.rectangle(
            imgResult,
            (x - offset, y - offset),
            (x + w + offset, y + h + offset),
            (255, 0, 255),
            3,
        )
        # Display fotogram to create a video
        cv2.imshow("Video", fotogram)
        cv2.imshow("Classifier Result", imgResult)
        cv2.waitKey(1)
        #TODO: Create, import and use the model


if __name__ == "__main__":
    main()
