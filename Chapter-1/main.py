# Import necessary libraries
import cv2 as cv

# To read image
image = cv.imread('image.jpeg')

# To display image
cv.imshow('Your image is: ',image)

# In order to wait for response
# Here waitKey takes argument in milliseconds in which you want to hold response
# Here 0 is a special character means to hold reponse forever
# To exit your response press 'q'
cv.waitKey(0)