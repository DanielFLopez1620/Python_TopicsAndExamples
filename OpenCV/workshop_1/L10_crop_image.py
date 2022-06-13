import cv2
from path_helps import get_path

def main():
    # Obtain path of the image
    my_img = "pexels_umbrellas.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)

    # Read image with cv2
    image = cv2.imread(file_path)

    # Crop image taking advantage of the matrix [height, width]
    cropImage = image[0:200,100:300]

    # Display image
    cv2.imshow("Image_Example", image)
    cv2.imshow("Image_Cropped", cropImage)
    # Generate a delay
    cv2.waitKey(0);


if __name__ == '__main__':
    main()