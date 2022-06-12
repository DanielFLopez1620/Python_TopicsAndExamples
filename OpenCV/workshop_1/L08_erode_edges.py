import cv2
import numpy as np

from path_helps import get_path

def main():
    my_img = "pexels-sharing.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)
    
    image = cv2.imread(file_path)

    imgEdge = cv2.Canny(image,100,200)
    
    # Dilate edges
    kernel = np.ones((5,5),np.uint8)
    imgDilatation = cv2.dilate(imgEdge, kernel, iterations = 1)
    
    # Erode edges
    imgErode = cv2.erode(imgDilatation, kernel, iterations = 1)

    cv2.imshow("Example", imgErode)
    cv2.waitKey(0);


if __name__ == '__main__':
    main()

    