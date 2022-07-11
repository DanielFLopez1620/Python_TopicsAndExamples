"""
Author: Murtaza's Workshop - Robotics and AI
Link: https://youtu.be/3xfOa4yeOb0?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5
Modified and commented by: Daniel Lopez
"""
import cv2
from cvzone.HandTrackingModule import HandDetector

def main():
    # Get videocapture from default camera
    webcam = cv2.VideoCapture(0)

    # Define hand detector
    handDetector = HandDetector(detectionCon = 0.8, maxHands = 2)
    while True:
        # Read current image captured by webcam
        success, fotogram = webcam.read()

        # Detect hands
        hands, fotogram = handDetector(fotogram)
        # hands, fotogram = handDetector(fotogram, draw = False)
        # hands, fotogram = handDetector(fotogram, flipType = True)

        """
        Information: 
        hand is a dict that contains --> lmList, bbox, center, type.
        * lmList: List of 21 landmark points of the hand (fingers and palms).
        * bbox: Information of the bounding box (x,y, width, height).
        * center: Gives the position (x,y) of the center hand.
        * type: Indicates whether the hand is right or left
        """

        # Reading and using information from the first hand
        if hands:
            firstHand = hands[0]
            firstLmList = firstHand["lmList"]
            firstBbox = firstHand["bbox"]
            firstCenter = firstHand["center"]
            firstType = firstHand["Type"]
            firstFingersUp = handDetector.fingersUp(firstHand)

            # Obtain the distance between fingers
            length, info, fotogram = handDetector.findDistance(firstLmList[8], firstLmList[12], fotogram)


        # Reading and using information from the second hand (if exists)
        if len(hands) == 2:
            secondHand = hands[1]
            secondLmList = secondHand["lmList"]
            secondBbox =secondHand["bbox"]
            secondCenter =secondHand["center"]
            secondType =secondHand["Type"]
            secondFingersUp = handDetector.fingersUp(secondHand)

        
        # Display info of the hand in terminal
        print(f"{firstType}:{firstFingersUp}\t|\t{secondType}:{secondFingersUp}")

         # Obtain the distance between hands (fingers or centerPoint)
        length, info, fotogram = handDetector.findDistance(firstLmList[8], secondLmList[8], fotogram)

        # Display image from webcam
        cv2.imshow("Webcam", fotogram)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()