
from turtle import st
import cv2
import numpy as np
from path_helps import get_path
from joining_images import stackImages


def getContours(image, imgCnt):
    # Obtain contours and its hierarchy
    # findContours params: image, retrition, aproximation
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    # Loop to describe the figures detected
    for i, cnt in enumerate(contours):
        # Obtain the area of the contour 
        area = cv2.contourArea(cnt)

        # Minimun threshold to draw a figure
        if area > 500:
            # Draw contour on a copy of image
            # drawContour params: image, contour, all?, color (BGR), thickness
            cv2.drawContours(imgCnt, cnt, -1, (255,0,0), 3)

            # Obtain the perimeter of the contour (length of arc)
            perimeter = cv2.arcLength(cnt,True)
            print(f"Figure #{i}:\n\tArea: {area}\n\tPerimeter: {perimeter}")

            # Generate an approximation of the figure's corners
            # aproxxPolyDP params: contour, resolution
            corners = cv2.approxPolyDP(cnt , 0.02*perimeter, True)
            numCorn = len(corners)
            print(f"\tCorners:{numCorn}")

            # Make an approximation of a rectangle that encloses the figure 
            x, y, w, h = cv2.boundingRect(corners) 
            cv2.rectangle(imgCnt,(x,y),(x+w,y+h),(0,255,0), 2)       

            # Decision about the figure:
            if numCorn == 3:
                figureType = "Triangle"
            elif numCorn == 4 and w/h > 0.95 and w/h < 1.05:
                figureType = "Square"
            elif numCorn == 4:
                figureType = "Quadrilateral"  
            elif numCorn > 7:
                figureType = "Circle"
            else: 
                figureType = "Unknown"
            print(f"\tFigure: {figureType}")

            # Add text to image
            cv2.putText(imgCnt, figureType, (x+(w//2)-10, y+(h//2)-10),
                 cv2.FONT_HERSHEY_COMPLEX, 0.5, (10,10,10), 2)
    return imgCnt



def main():
    # Obtain path of the image
    my_img = "shapes.png"
    folder = "resources"
    file_path = get_path(my_img, folder)

    # Read image with cv2
    image = cv2.imread(file_path)

    # Transform image to detect edges
    imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    imgBlank = np.zeros_like(image)
    imgCnt = image.copy()

    # Call function to identy countours and next the figure
    imgCnt = getContours(imgCanny, imgCnt)
    
    # Display all images
    final_image = stackImages(0.5, [[image,imgGray,imgBlur],[imgCanny,imgBlank,imgCnt]])
    cv2.imshow("Collage", final_image)
    cv2.waitKey(0);


if __name__ == '__main__':
    main()