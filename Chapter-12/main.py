# Import necessary libraries
import cv2 as cv
import numpy as np

# Creating a capture object
# Reading Frames from camera
cap = cv.VideoCapture(0)

# Writing format, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
writer = cv.VideoWriter("output.mp4", cv.VideoWriter_fourcc("M", "J", "P", "G"), 10, (frame_width, frame_height))

# Reading and playing video
while(cap.isOpened()):
    
    # Capture Frame by Frame
    ret, frame = cap.read()

    if ret == True:
        # To write each Frame
        writer.write(frame)

        # To display each BGR Frame
        cv.imshow('OriginalCam', frame)

        # To quit with 'q' key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()