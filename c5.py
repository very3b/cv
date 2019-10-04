import numpy as np
import cv2


#img=cv2.imread('data/messi5.jpg', 0)
cap= cv2.VideoCapture(0)

if cap.isOpened():
    pass
else:
    cap.open(0)

while(True):
    ret, frame =cap.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)

    cv2.waitKey(0)
    break


cap.release()
cv2.destroyAllWindows()
