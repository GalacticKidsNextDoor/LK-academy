import numpy as np
import cv2 as cv


drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1


# mouse callback function
def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
            
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_rectangle)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'[ Paint Rectangles ]',(15,420), font, 1,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'Click and drag mouse to draw',(30,445), font, 0.7,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'Press "m" to toggle fill mode',(30,470), font, 0.7,(255,255,255),2,cv.LINE_AA)
cv.putText(img,'Press "q" to exit',(30,495), font, 0.7,(255,255,255),2,cv.LINE_AA)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1)
    if k == ord('m'):
        mode = not mode
    elif k == ord("q"):
        break
        
cv.destroyAllWindows()