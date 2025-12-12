import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)

cv.circle(img,(447,63), 63, (0,0,255), -1)

cv.imshow('frame', img)

k = cv.waitKey(0)