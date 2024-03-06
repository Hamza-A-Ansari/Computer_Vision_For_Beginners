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
        cv.imshow("Vide", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release capture object
cap.release()
# Destroy all windows
cv.destroyAllWindows()