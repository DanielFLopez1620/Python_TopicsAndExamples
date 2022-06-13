
import cv2
import numpy as np
from path_helps import get_path

def main():
    # Obtain path of the image
    my_img = "pexels_cards.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)

    # Read image with cv2
    image = cv2.imread(file_path)

    # Display image
    cv2.imshow("Image_Example", image)

    # Generate a delay: (0) is infinite or specify a time in ms
    cv2.waitKey(0);

    # Definition of points for perspective
    # points = np.float32([[],[],[],[]])


if __name__ == '__main__':
    main()