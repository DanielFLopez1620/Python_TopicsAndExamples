import cv2
import numpy as np
from path_helps import get_path
from joining_images import stackImages

def empty(a):
    pass


def main():
    # Obtain path of the image
    my_img = "pexels_umbrellas.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)

    # Creating trackbars, with a base color filter
    window_h = 640
    window_w = 260
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", window_w, window_h)
    cv2.createTrackbar("Hue_Min", "TrackBars", 0, 179, empty)
    cv2.createTrackbar("Hue_Max", "TrackBars", 19, 179, empty)
    cv2.createTrackbar("Sat_Min", "TrackBars", 110, 255, empty)
    cv2.createTrackbar("Sat_Max", "TrackBars", 245, 255, empty)
    cv2.createTrackbar("Val_Min", "TrackBars", 153, 255, empty)
    cv2.createTrackbar("Val_Max", "TrackBars", 255, 255, empty)

    # Main loop for the color isolation
    while True:
        # Obtain info from the trackbars
        hue_min = cv2.getTrackbarPos("Hue_Min","TrackBars")
        hue_max = cv2.getTrackbarPos("Hue_Max","TrackBars")
        sat_min = cv2.getTrackbarPos("Sat_Min","TrackBars")
        sat_max = cv2.getTrackbarPos("Sat_Max","TrackBars")
        val_min = cv2.getTrackbarPos("Val_Min","TrackBars")
        val_max = cv2.getTrackbarPos("Val_Max","TrackBars")

        # Read image with cv2 and convertion to HSV
        image = cv2.imread(file_path)
        imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Generating a mask
        lower = np.array([hue_min,sat_min,val_min])
        upper = np.array([hue_max,sat_max,val_max])
        mask = cv2.inRange(imgHSV, lower, upper)

        # Isolating the color, using and for pixels present in both images
        imgIso = cv2.bitwise_and(image, image, mask=mask)
                
        # Display image
        final_image = stackImages(1.0, [image,imgIso])
        cv2.imshow("Color_Isolation", final_image)
        cv2.waitKey(1);


if __name__ == '__main__':
    main()