# Import necessary libraries
import cv2 as cv
import numpy as np

# Creating a capture object
cap = cv.VideoCapture('Venice_10.mp4')

# Total number of Frames in Video
frames = cap.get(cv.CAP_PROP_FRAME_COUNT)

# Frames per second of Video
fps = cap.get(cv.CAP_PROP_FPS)

# Height and Width of frame
frame_height = int(cv.CAP_PROP_FRAME_HEIGHT)
frame_width = int(cv.CAP_PROP_FRAME_WIDTH)

# Initiating the output writer for Video
fourcc = cv.VideoWriter_fourcc(*'MJPG')
writer = cv.VideoWriter('reversed.avi', fourcc, fps, (frame_width, frame_height), isColor=False)

# To check the nuymber of Frames and FPS in our video
print(f'Number of Frames are: {frames}')
print(f'FPS is: {fps}')

# We get the index of the last Frame of video
frame_index = frames - 1

# Reading and playing video
if (cap.isOpened()):
    while(frame_index != 0):

        # We set the current Frame position to last Frame
        cap.set(cv.CAP_PROP_POS_FRAMES, frame_index)

        ret, frame = cap.read()
        if ret == True:

            # Resize the Frame
            # frame = cv.resize(frame, (frame_width*0.5, frame_height*0.5))

            # To write each Frame
            writer.write(frame)

            # Decrementing Frame index
            frame_index = frame_index - 1

            # Printing the progress
            if frame_index % 10 == 0:
                print(frame_index)

            # To quit with 'q' key
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
else:
    print('Error in reading video')

# Release capture object
cap.release()
# Release writer object
writer.release()
# Destroy all windows
cv.destroyAllWindows()