import cv2

def main():
    # Select default webcam
    video = cv2.VideoCapture(0)

    # Set height
    video.set(4,480)

    # Set width
    video.set(3,640)
    
    # Set brightness
    video.set (10,100)

    
    # Loop to run the video
    while True:
        # Convert and read sequence
        success, fotogram = video.read()
        cv2.imshow("Video_Example", fotogram)

        # Option to stop the reproduction
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()