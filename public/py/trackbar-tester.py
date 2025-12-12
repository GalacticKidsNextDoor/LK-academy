import numpy as np
import cv2 as cv
def youShallNot(x):
    pass
    
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('My Color Picker')

# create trackbars for color change
cv.createTrackbar('R','My Color Picker',0,255,youShallNot)
cv.createTrackbar('G','My Color Picker',0,255,youShallNot)
cv.createTrackbar('B','My Color Picker',0,255,youShallNot)

# create switch for ON/OFF functionality
cv.createTrackbar('switch', 'My Color Picker',0,1,youShallNot)

while(1):
    cv.imshow('My Color Picker',img)
    k = cv.waitKey(20)
    if k == ord("q"):
        break
        
    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','My Color Picker')
    g = cv.getTrackbarPos('G','My Color Picker')
    b = cv.getTrackbarPos('B','My Color Picker')
    s = cv.getTrackbarPos('switch','My Color Picker')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
        
cv.destroyAllWindows()