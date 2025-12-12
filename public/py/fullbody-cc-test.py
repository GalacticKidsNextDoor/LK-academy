from __future__ import print_function
import cv2 as cv
import argparse

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect torsos
    torsos = fullbody_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in torsos:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
    cv.imshow('Capture - Face detection', frame)

parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')

parser.add_argument('--fullbody_cascade', help='Path to face cascade.', default='./data/haarcascades/haarcascade_fullbody.xml')

parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
fullbody_cascade_name = args.fullbody_cascade
fullbody_cascade = cv.CascadeClassifier()


#-- 1. Load the cascades
if not fullbody_cascade.load(cv.samples.findFile(fullbody_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)

camera_device = "../media/vid/ongoly-hs.mp4"
#args.camera

#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == ord("q"):
        break