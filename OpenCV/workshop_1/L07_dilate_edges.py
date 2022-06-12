import cv2
import numpy as np

from path_helps import get_path

def main():
    my_img = "pexels-sharing.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)
    
    image = cv2.imread(file_path)

    # Obtain edges of the image
    imgEdge = cv2.Canny(image,100,200)

    # Define a kernel
    kernel = np.ones((5,5),np.uint8)

    # Improve managment of edges
    # dilate params: image (Canny), kernel, iterations (Reviews over image)
    imgDilatation = cv2.dilate(imgEdge, kernel, iterations = 1 )
    
    cv2.imshow("Example", imgDilatation)
    cv2.waitKey(0);


if __name__ == '__main__':
    main()