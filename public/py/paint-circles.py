import numpy as np
import cv2 as cv

# mouse callback function
#
#LBUTTONDBLCLK
#
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),10,(255,0,0),-1)
        
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Plant Circles!',(15,420), font, 1,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'Left click to stamp blue circles',(30,460), font, 0.7,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'Press "q" to exit',(30,500), font, 0.7,(255,255,255),2,cv.LINE_AA)

while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) == ord("q"):
        break
        
cv.destroyAllWindows()