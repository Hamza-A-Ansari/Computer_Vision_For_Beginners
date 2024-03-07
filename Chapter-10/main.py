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
        # To display each Frame
        cv.imshow('Frame', frame)

        # To quit with 'q' key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()