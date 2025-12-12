import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)

cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

cv.imshow('frame', img)

k = cv.waitKey(0)