import cv2
import numpy as np
from joining_images import stackImages

def preProcessingEdges(image):
    
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageBlur = cv2.GaussianBlur(imageGray, (5,5), 1)
    imageEdges = cv2.Canny(imageBlur, 200, 200)
    
    kernel = np.ones((5,5))
    imageDilat = cv2.dilate(imageEdges, kernel, iterations = 2)
    imageErode = cv2.erode(imageDilat, kernel, iterations = 1)

    return imageErode


def getContoursSheet(image, imgCnt):
    maxArea = 0
    biggest = np.array([])
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)

        if area > 2000:
            perimeter = cv2.arcLength(cnt,True)
            corners = cv2.approxPolyDP(cnt , 0.02*perimeter, True)
            numCorners = len(corners)

            if numCorners == 4 and area > maxArea:
                biggest = corners
                maxArea = area

    cv2.drawContours(imgCnt, biggest, -1, (0,0,255), 5)
    return biggest, imgCnt


def reorderCnt (points):
    points = points.reshape((4,2))
    contour = np.zeros((4,1,2), np.int32)
    
    addPairs = points.sum(1)
    contour[0] = points[np.argmin(addPairs)]
    contour[3] = points[np.argmax(addPairs)]

    diffPairs = np.diff(points, axis = 1)
    contour[1] = points[np.argmin(diffPairs)]
    contour[2] = points[np.argmin(diffPairs)]
    return contour


def getWarpPersp(image, contour, width, height):
    points = contour
    wrap = np.float32([[0,0],[width,0],[0,height],[width,height]])

    transform = cv2.getPerspectiveTransform(points, wrap)
    imgWrap = cv2.warpPerspective(image, transform, (width,height))

    return imgWrap


def main():
    # Select default webcam
    video = cv2.VideoCapture(0)
    width = 640
    height = 480

    # Video settings
    video.set(4, height)
    video.set(3,width)
    video.set (10,150)
    
    # Loop to run the video
    while True:
        # Convert and read sequence
        success, fotogram = video.read()
        fotogram = cv2.resize(fotogram,(width, height))

        # Preprocessing
        imageEdges = preProcessingEdges(fotogram)

        # Contours
        imageThreshold = imageEdges.copy()
        imageCnt = fotogram.copy()
        docCnt, imageCnt = getContoursSheet(imageThreshold, imageCnt)

        # Warp perspective
        docCnt = reorderCnt(docCnt)
        docPerps = getWarpPersp(fotogram, docCnt, width, height)
        # docPerps = fotogram.copy()
        
        # Display results
        results = stackImages(0.6,[[fotogram, imageCnt],[imageThreshold, docPerps]])
        cv2.imshow("Document_Scanner", results)

        # Option to stop the reproduction
        if cv2.waitKey(1) and (0xFF == ord('q') or not success):
            break


if __name__ == '__main__':
    main()