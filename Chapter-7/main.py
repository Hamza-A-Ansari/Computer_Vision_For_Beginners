# Import necessary libraries
import cv2 as cv
import numpy as np

# Creating a capture object
cap = cv.VideoCapture('Venice_10.mp4')

# Indicator
if (cap.isOpened() == False):
    print("Error in reading video")

# Reading and playing video
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        # Convert each BGR frame to Grayscale
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Convert each Gray frame to Black & White
        (thresh, bw_frame) = cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY)

        # To show each frame
        cv.imshow("Vide", bw_frame)
        # cv.imshow("Vide", gray_frame)

        # To quit with 'q' key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release capture object
cap.release()
# Destroy all windows
cv.destroyAllWindows()