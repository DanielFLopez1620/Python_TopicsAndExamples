
import cv2
from path_helps import get_path

def main():
    # Obtain path of the image
    my_img = "pexels_umbrellas.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)

    # Read image with cv2
    image = cv2.imread(file_path)
    
    # Display info of the image (size)
    print(f"Original image: {image.shape}\n(height, width, channels)")
    
    # Resize the image, params: (image to resize, (width, heigh))
    resize = cv2.resize(image, (300, 200))
    print(f"Resized image: {image.shape}")
    # Display image
    cv2.imshow("Image_Example", image)
    cv2.imshow("Image_Resize", resize)

    # Generate a delay
    cv2.waitKey(0);


if __name__ == '__main__':
    main()