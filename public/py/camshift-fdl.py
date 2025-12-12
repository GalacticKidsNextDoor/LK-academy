import sys
import numpy as np
import cv2 as cv
    
def main(argv):
    if (len(sys.argv) < 5):
        print('Not enough parameters!')
        print('Usage:\n>> camshift-fdl.py <source_video> roi_x roi_y roi_width roi_height')
        return -1
    

    cap = cv.VideoCapture(sys.argv[1])

    # take first frame of the video
    ret,frame = cap.read()
    
    # setup initial location of window
    x, y, w, h = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    
    #x, y, w, h = 
    #FDL 0 - FEET(500 150 75 100) 
    #      - LOWER_LEGS(500 100 75 100)
    #      - UPPER_LEGS(500 50 75 100)
    #      - TORSO/FULL_BODY(500 0 75 100)
    #
    #FDL 1 - 750 200 75 75 
    #FDL 2 - 450, 310, 80, 120 
    
    track_window = (x, y, w, h)
    # set up the ROI for tracking
    roi = frame[y:y+h, x:x+w]
    cv.imshow("Selected ROI", roi)

    hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
    roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
    cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
    # Setup the termination criteria, either 10 iteration or move by at least 1 pt
    term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

    while(1):
        ret, frame = cap.read()
        if ret == True:
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
            # apply camshift to get the new location
            ret, track_window = cv.CamShift(dst, track_window, term_crit)
            # Draw it on image
            pts = cv.boxPoints(ret)
            pts = np.int0(pts)
            img2 = cv.polylines(frame,[pts],True, 255,2)

            #cv.rectangle(img2,(420,280),(500,400),(255,0,0),3)

            cv.imshow('img2',img2)
            k = cv.waitKey(30)
            if k == ord("q"):
                break
        else:
            break
        
if __name__ == "__main__":
    main(sys.argv[1:])