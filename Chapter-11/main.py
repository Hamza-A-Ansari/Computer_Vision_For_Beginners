# Import necessary libraries
import cv2 as cv
import numpy as np

# Creating a capture object
# Reading Frames from camera
cap = cv.VideoCapture(0)

# Reading and playing video
while(cap.isOpened()):
    
    # Capture Frame by Frame
    ret, frame = cap.read()

    if ret == True:
        # Convert each BGR frame to Grayscale
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Convert each Gray frame to Black & White
        (thresh, bw_frame) = cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY)

        # To display each BGR Frame
        cv.imshow('OriginalCam', frame)

        # To display each Gray Frame
        cv.imshow('GrayCam', gray_frame)

        # To display each Balck & White Frame
        cv.imshow('B&WCam', bw_frame)

        # To quit with 'q' key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()