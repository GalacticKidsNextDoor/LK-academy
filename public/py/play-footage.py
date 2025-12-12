import numpy as np
import cv2 as cv

print("Video Capture \n author: Patrice-Morgan \n v 0.1.0 \n\n")

cap = cv.VideoCapture('../media/vid/Ongoly2011.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
        
cap.release()
cv.destroyAllWindows()