import cv2
from path_helps import get_path_resources

def main():
    # Read image
    my_img = "pieces_2.jpg"
    file_path = get_path_resources(my_img)
    image = cv2.imread(file_path)
    
    # Resize image
    scale = 0.22
    width = int(image.shape[1]*scale)
    height = int(image.shape[0] * scale)
    resize = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)

    # Obtain edges of the image
    imgEdge2 = cv2.Canny(resize,250,350)
    
    # Display results
    cv2.imshow("Edges2", imgEdge2)
    cv2.waitKey(0);


if __name__ == '__main__':
    main()