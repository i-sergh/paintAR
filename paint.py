import cv2
import numpy as np


cnv = np.zeros( (480, 640, 3), dtype=np.uint8())

cap = cv2.VideoCapture(0)

def findContour(clr_low, clr_high, hsv, out, cnv, clr):
    mask = cv2.inRange(hsv, clr_low, clr_high)
    
    cont, h = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )

    cont = sorted(cont, key=cv2.contourArea, reverse=True)
    if len(cont)> 0:
        for i , cn in enumerate(cont):
            if cv2.contourArea(cn) > 1000:
                cv2.drawContours(out, cont, i, clr, 2)
                cv2.drawContours(cnv, cn, -1, clr, -1) 


while True:
    tr, frame = cap.read()

    frame = cv2.flip(frame, 2)
    frame_ = cv2.blur(frame, (10,10) )
    frame_HSV = cv2.cvtColor( frame_, cv2.COLOR_BGR2HSV )

    findContour( (0,190, 70), (15,255,255),
                 frame_HSV, frame, cnv, (0,0,255))
    findContour( (15,190, 70), (40,255,255),
                 frame_HSV, frame, cnv, (0,255,255))
    #findContour( (0,190, 70), (15,255,255),
    #             frame_HSV, frame, cnv, (0,0,255))
    
    cv2.imshow('paint', cnv)
    cv2.imshow('camera', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    if key == 113:
        cnv = np.zeros( (480, 640, 3), dtype=np.uint8())
        
    
cv2.destroyAllWindows()
cap.release()
