import cv2
from path_helps import get_path

def main():
    # Obtain path of the file
    my_img = "pexels_sharing.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)

    # Convert image to an object
    image = cv2.imread(file_path)

    # Obtain gray scales image
    imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Display image
    cv2.imshow("GrayScale", imgGray)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
