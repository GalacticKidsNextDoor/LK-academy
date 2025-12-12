from __future__ import print_function
import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()

if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN()
    
capture = cv.VideoCapture("../media/vid/copa-seq-2-wr.mp4")

font = cv.FONT_HERSHEY_SIMPLEX
fontSize = 2
fontThickness = 3

if not capture.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)
    
while True:
    ret, frame = capture.read()
    if frame is None:
        break
    
    fgMask = backSub.apply(frame)
    
    #cv.rectangle(fgMask, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(fgMask, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 500),
               font, fontSize, (255,255,255), fontThickness, cv.LINE_AA)
    
    
    #cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    
    keyboard = cv.waitKey(30)
    if keyboard == ord("q"):
        break