
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

    # Print info of the image
    print(image.shape)
    width, height = 255, 350

    # Try lines to identify edges of the card:
    # cv2.line(image, (432,76), (358,248), (0,0,255), 2)
    # cv2.line(image, (358,248), (516,317), (0,255,255), 2)
    # cv2.line(image, (432,76), (567,126), (255,0,255), 2)

    # Using four points to make the wrap
    points = np.float32([[432,76],[567,126],[358,248],[516,317]])
    wrap = np.float32([[0,0],[width,0],[0,height],[width,height]])

    # Transformation
    transform = cv2.getPerspectiveTransform(points, wrap)
    imgWrap = cv2.warpPerspective(image, transform, (width,height))

    # Display image
    cv2.imshow("Image_Example", image)
    cv2.imshow("Wrapped image", imgWrap)
    cv2.waitKey(0);


if __name__ == '__main__':
    main()