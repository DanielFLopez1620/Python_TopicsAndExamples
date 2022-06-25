import cv2
import numpy as np
from joining_images import stackImages

def preProcessingEdges(image):
    """
    Proprocess the image to recognize the edges
    
    image --> THe matriz or cv2 image to preprocess
    return imageErode --> Image with the edges eroded
    """
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageBlur = cv2.GaussianBlur(imageGray, (5,5), 1)
    imageEdges = cv2.Canny(imageBlur, 200, 200)
    
    kernel = np.ones((5,5))
    imageDilat = cv2.dilate(imageEdges, kernel, iterations = 2)
    imageErode = cv2.erode(imageDilat, kernel, iterations = 1)

    return imageErode


def getContoursSheet(image, imgCnt):
    """
    Get the available contours and search for posible sheets or documents

    image --> Matriz or cv2 image processed to have only contours
    imgCnt --> Image that want to be processed
    return biggest --> Biggest rectangular contour candidate to be a document
    return imgCnt --> Original image with the rectangular contour given
    """
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
    """
    Reorder the points/corners of the contour to display document

    points --> The biggest point given by getContoursSheet function
    return contour --> The biggest rectangular points reorganized
    """
    points = points.reshape((4,2))
    contour = np.zeros((4,1,2), np.int32)
    
    addPairs = points.sum(1)
    contour[0] = points[np.argmin(addPairs)]
    contour[3] = points[np.argmax(addPairs)]

    diffPairs = np.diff(points, axis = 1)
    contour[1] = points[np.argmin(diffPairs)]
    contour[2] = points[np.argmin(diffPairs)]
    return contour


def getWarpPersp(image, contour, width, height, cropPix):
    """
    Get the warp perspective of the document given

    image --> Original image that has the document
    contour --> The bigget contour posible to be a doc recognized
    width --> Width of the original image
    height --> Height of the original image
    cropPix --> Number of pixel to cut in the edges to fix them
    return imgCrop --> The perspective of the document cropped
    """
    points = contour
    wrap = np.float32([[0,0],[width,0],[0,height],[width,height]])

    transform = cv2.getPerspectiveTransform(points, wrap)
    imgWrap = cv2.warpPerspective(image, transform, (width,height))

    imgCrop = imgWrap[20:imgWrap.shape[0]-cropPix, 20:imgWrap.shape[1]-cropPix]
    imgCrop = cv2.resize(imgCrop, (width, height))
    
    return imgCrop



def main():
    # Select default webcam
    video = cv2.VideoCapture(0)
    width = 640 # 480
    height = 480 # 640
    cropPix = 20

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
        
        # Verify recognition
        if docCnt.size != 0:
            # Warp perspective
            docCnt = reorderCnt(docCnt)
            docPerps = getWarpPersp(fotogram, docCnt, width, height, cropPix)
            results = stackImages(0.6,[[fotogram, imageCnt],[imageThreshold, docPerps]])
        else:
            results = stackImages(0.6,[[fotogram, fotogram],[fotogram, fotogram]])
        
        # Display results
        cv2.imshow("Document_Scanner", results)

        # Option to stop the reproduction
        if cv2.waitKey(1) and (0xFF == ord('q') or not success):
            break


if __name__ == '__main__':
    main()