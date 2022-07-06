"""
Author: Murtaza's Work - Robotics and AI
--> https://youtu.be/CKmAZss-T5Y?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5

Modified and commented by: Daniel Lopez
"""
#TODO: Install dependencies in Ubuntu

import cv2
import os
from cvzone.HandTrackingModule import HandDetector
from path_helps import get_path
import numpy as np

def main():
    # Definitions
    width_cam, height_cam = 1280, 720
    slideNumber = 0
    multiplier = 1
    width_min, height_min = int(213 * multiplier), int(120 * multiplier)
    gestureThreshold = 300
    buttonPressed = False
    buttonCounter = 0
    buttonDelay = 40

    # List of images
    # TODO: Indicate the path and add files order
    folderPath = ""
    pathImages = os.listdir()
    slidePath = "" 

    # Capture webcam video
    webcam = cv2.VideoCapture(0)
    webcam.set(3, width_cam)
    webcam.set(4, height_cam)

    # Hand detector definition
    detectHand = HandDetector(detectionCon=0.8, maxHands=1)

    while True:
        # Read camara info and invert camera
        success, fotogram = webcam.read()
        fotogram = cv2.flip(fotogram, 1)

        # Import slides
        # TODO: Joint path of inage
        currentSlidePath = ""
        currentSlide = cv2.imread(currentSlidePath)

        # Adding webcam image on slide
        camWindow = cv2.resize(fotogram, (width_cam, height_min))
        height_sli, width_sli = currentSlide.shape
        currentSlide[0 : height_min,
                     width_sli - width_min: width_sli] = camWindow
        
        # Detect hand
        hands, fotogram = detectHand.findHands(fotogram)
        cv2.line(fotogram,(0, gestureThreshold), (width_cam, gestureThreshold), (0, 255, 0), 10)

        # Conditional for reading hands positions
        if hands and not buttonPressed:
            # Identify fingers raised
            hand = hands[0]
            fingersUp = detectHand.fingersUp(hand)
            center_x, center_y = hand['center']
            print(f"Fingers up: {fingersUp}")

            # Identify the index finger position
            lmList = hand['lmList']
            fingerIndex = lmList[8][0], lmList[8][1]

            # Constraint values for using index finger
            xVal = np.interp(lmList[8][0], (width_cam // 2, width_cam), [0, width_cam])
            # <--

            # Verify if the gesture is in the correct region
            if center_y <= gestureThreshold:
                # Gesture 1: Change to previous slide
                if fingersUp == [1, 0, 0, 0, 0]:
                    if slideNumber > 0:
                        slideNumber -=1
                    print("Left")
                    buttonPressed = True

                # Gesture 2: Change to next slide
                elif fingersUp == [0, 0, 0, 0, 1]:
                    print("Rigth")
                    slideNumber +=1
                    buttonPressed = True

            # Gesture 3: Show Pointer
            if fingersUp == [0, 1, 1, 0, 0]:
                cv2.circle(currentSlide, fingerIndex, 12, (0,0,255), cv2.FILLED)

        # Verify button and the iterations, make a delay
        if buttonPressed:
            buttonCounter += 1
            if buttonCounter > buttonDelay:
                buttonCounter = 0
                buttonPressed = False

        # Show video by fotograms and the presentation
        cv2.imshow("Video", fotogram)
        cv2.imshow("Presentation", currentSlide)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break


if __name__ == "__main__":
    main()