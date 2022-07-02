"""
Author: Murtaza's Work - Robotics and AI
--> https://youtu.be/WQeoO7MI0Bs?list=PLxYZ6JuFZuoZPUEUtcUL0YoAYRvnNLAG5

Modified and commented by: Daniel Lopez
"""

import cv2
import numpy as np


def getContour2Paint(image):
    """
    Obtain the position of the paint depending on the color

    image --> Image masked to identify the colors
    return (x-w)//2 --> X position of the pincel in image
    return y --> Y position of the pincel in image
    """
    x, y, w, h = 0, 0, 0, 0
    contours, hierarchy = cv2.findContours(
        image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(image, cnt, -1, (255,0,0), 3)
            perimeter = cv2.arcLength(cnt, True)
            corners = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(corners)
            # cv2.imshow("Contours", image)
    return x, y


def drawAndPaint(image, colorPoints, colorBGR):
    """
    Add the pencil markers (draw) to the board

    image --> Original fotogram/image read
    colorPoints --> Array of points to paint
    colorBGR --> Array that indicates the correspond color in BGR
    return image --> Image painted
    """
    for point in colorPoints:
        cv2.circle(image, (point[0], point[1]), 10, colorBGR[point[2]],
                   cv2.FILLED)
    return image


def paintColor(image, colorsHSV, colorBGR):
    """
    Obtaine the points to paint and the correspondent color to each point

    image --> Original image/fotogram read
    colorHSV --> Array of the color pattern to apply as filter
    colorBGR --> Arrray that indicates the correspondent color in BGR
    return points --> Points of markers/pincels read with the webcam
    """
    colorList = ("Orange", "Purple", "Green")
    points = []  # [x, y, color] of each color
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    for i, color in enumerate(colorsHSV):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        # cv2.imshow(str(colorList[i]), mask)
        x, y = getContour2Paint(mask)
        cv2.circle(image, (x, y), 10, colorBGR[i], cv2.FILLED)
        if x != 0 and y != 0:
            points.append([x, y, i])
    return points


def main():
    # Definition of the colors for the program
    colorsPaints = [  # H_min, S_min, V_min, H_max, S_max, V_max
        [0, 143, 155, 26, 255, 255],  # Orange
        [105, 76, 117, 141, 164, 207],  # Purple
        [63, 113, 109, 103, 255, 255],  # Green
    ]
    colorBGR = [[51, 153, 255], [255, 0, 255], [0, 255, 0]]
    # colorList = ("Orange", "Purple", "Green")

    # Painted points
    onBoard = []

    # Capture video of the default web cam
    video = cv2.VideoCapture(0)

    # Configuration of the video web cam
    camWidth = 640
    camHeigth = 480
    video.set(4, camHeigth)
    video.set(3, camWidth)
    video.set(10, 150)

    # Loop to run the video
    while True:
        # Convert and read sequence
        success, fotogram = video.read()
        imgPainted = fotogram.copy()
        # Identify colors
        points = paintColor(imgPainted, colorsPaints, colorBGR)

        # Paint the colors
        if len(points) != 0:
            for newP in points:
                onBoard.append(newP)
        if len(onBoard) != 0:
            imgPainted = drawAndPaint(fotogram, onBoard, colorBGR)
        # Display video and virtual paint
        cv2.imshow("Painted_Board", imgPainted)

        # Option to stop the reproduction
        if cv2.waitKey(1) and (0xFF == ord("q") or not success):
            break


if __name__ == "__main__":
    main()
