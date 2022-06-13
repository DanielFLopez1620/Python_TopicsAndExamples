import cv2
import numpy as np

from path_helps import get_path

def main():
    # Obtain path of image
    my_img = "pexels_sharing.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)
    
    # Read image as cv2 object
    image = cv2.imread(file_path)

    # Obtain edges of the image
    imgEdge = cv2.Canny(image,100,200)

    # Define a kernel
    kernel = np.ones((5,5),np.uint8)

    # Improve managment of edges
    # dilate params: image (Canny), kernel, iterations (Reviews over image)
    imgDilatation = cv2.dilate(imgEdge, kernel, iterations = 1 )
    
    # Display image
    cv2.imshow("Dilatation", imgDilatation)
    cv2.waitKey(0);


if __name__ == '__main__':
    main()