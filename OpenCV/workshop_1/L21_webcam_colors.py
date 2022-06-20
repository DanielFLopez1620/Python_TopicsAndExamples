import cv2
import numpy as np
from joining_images import stackImages

def empty(a):
    pass


def main():
    # Select default webcam
    video = cv2.VideoCapture(0)

    # Video setting for webcam
    video.set(4,480)
    video.set(3,640)
    video.set (10,100)

    # Creating trackbars
    # Creating trackbars
    window_h = 280
    window_w = 240
    cv2.namedWindow("HSV_selector")
    cv2.resizeWindow("HSV_selector", window_w, window_h)
    cv2.createTrackbar("Hue_Min", "HSV_selector", 0, 179, empty)
    cv2.createTrackbar("Hue_Max", "HSV_selector", 10, 179, empty)
    cv2.createTrackbar("Sat_Min", "HSV_selector", 0, 255, empty)
    cv2.createTrackbar("Sat_Max", "HSV_selector", 10, 255, empty)
    cv2.createTrackbar("Val_Min", "HSV_selector", 0, 255, empty)
    cv2.createTrackbar("Val_Max", "HSV_selector", 10, 255, empty)


    # Loop to run the video
    while True:
        # Using the info of the trackbars
        hue_min = cv2.getTrackbarPos("Hue_Min","HSV_selector")
        hue_max = cv2.getTrackbarPos("Hue_Max","HSV_selector")
        sat_min = cv2.getTrackbarPos("Sat_Min","HSV_selector")
        sat_max = cv2.getTrackbarPos("Sat_Max","HSV_selector")
        val_min = cv2.getTrackbarPos("Val_Min","HSV_selector")
        val_max = cv2.getTrackbarPos("Val_Max","HSV_selector")

        # Read sequence and convert into HSV
        success, fotogram = video.read()
        HSVfotogram = cv2.cvtColor(fotogram, cv2.COLOR_BGR2HSV)
        
        # Using a mask
        lower = np.array([hue_min,sat_min,val_min])
        upper = np.array([hue_max,sat_max,val_max])
        HSVselected = cv2.inRange(HSVfotogram, lower, upper)
        HSVisolated = cv2.bitwise_and(fotogram, fotogram, mask=HSVselected)

        # Display fotogram in a stacked way
        videoCom = stackImages(0.6, [fotogram, HSVisolated])
        cv2.imshow("Video_Recognition", videoCom)

        # Option to stop the repHSV_selector
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()