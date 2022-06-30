import cv2
from path_helps import get_path

def main():
    # Obtain path of the image
    my_img = "pexels_person.jpg"
    folder = "resources"
    file_path = get_path(my_img, folder)
    
    # Read cascade
    faceCascade= cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")    # Read image with cv2
    
    # Read image
    image = cv2.imread(file_path)
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Dectect faces (frontal)
    facesDetected = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    
    # Define and add bounding boxes
    for (x,y,h,w) in facesDetected:
        cv2.rectangle(image, (x,y), (x+w,y+h), (255,255,0), 3)

    # Display image
    cv2.imshow("Output", image)
    cv2.waitKey(0);
    # TODO: Change base face

if __name__ == '__main__':
    main()