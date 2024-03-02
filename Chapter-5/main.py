# Import necessary libraries
import cv2 as cv
import numpy as np

# To read image
image = cv.imread('image.jpeg')

# To resize image
image = cv.resize(image, (500,500))

# Convert BGR image to Grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Convert Grayscale to Black & White
(thresh, bw_image) = cv.threshold(gray_image, 127, 255, cv.THRESH_BINARY)

# To display image
cv.imshow('Your BGR image is: ',image)
cv.imshow('Your Grayscale image is: ',gray_image)
cv.imshow('Your Black & White image is: ',bw_image)

# To save an image
cv.imwrite('black&white_image.png',bw_image)

# In order to wait for response
# Here waitKey takes argument in milliseconds in which you want to hold response
# Here 0 is a special character means to hold reponse forever
# To exit your response press 'q'
cv.waitKey(0)

# To destroy all windows
cv.destroyAllWindows()