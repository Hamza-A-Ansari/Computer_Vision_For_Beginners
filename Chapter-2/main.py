# Import necessary libraries
import cv2 as cv
import numpy as np

# To read image
image1 = cv.imread('image.jpeg')

# To resize image
image2 = cv.resize(image1, (500,500))

# To display image
cv.imshow('Your first image is: ',image1)
cv.imshow('Your second image is: ',image2)

# In order to wait for response
# Here waitKey takes argument in milliseconds in which you want to hold response
# Here 0 is a special character means to hold reponse forever
# To exit your response press 'q'
cv.waitKey(0)

# To destroy all windows
cv.destroyAllWindows()