import cv2
import numpy as np



cap = cv2.VideoCapture(0)

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540
cap.set(3, WINDOW_WIDTH)
cap.set(4, WINDOW_HEIGHT)


cnv = np.zeros( (WINDOW_HEIGHT, WINDOW_WIDTH, 3) , dtype=np.uint8())


def findContour(clr_low, clr_high, hsv, out, cnv, clr):
    mask = cv2.inRange(hsv, clr_low, clr_high)
    
    cont, h = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )

    if len(cont)> 0:
        for i , cn in enumerate(cont):
            if cv2.contourArea(cn) > 100:
                cv2.drawContours(out, cont, i, clr, 2)
                #cv2.drawContours(cnv, cn, -1, clr, -1)
                cv2.drawContours(cnv, cont, i, clr, -1)


while True:
    tr, frame = cap.read()

    frame = cv2.flip(frame, 2)
    frame_ = cv2.blur(frame, (20,20) )
    frame_HSV = cv2.cvtColor( frame_, cv2.COLOR_BGR2HSV )

    # red
    findContour( (0,150, 70), (7,255,255),
                 frame_HSV, frame, cnv, (0,0,255))
    # orange
    findContour( (7,150, 70), (15,255,255),
                 frame_HSV, frame, cnv, (0,100,250))
    # yellow
    findContour( (15,190, 70), (30,255,255),
                 frame_HSV, frame, cnv, (0,255,255))
    # light green
    findContour( (30, 150, 40), (65,255,255),
                 frame_HSV, frame, cnv, (50,255,100))
    # green
    findContour( (65, 170, 50), (90,255,255),
                 frame_HSV, frame, cnv, (50,125,10))
    # blue
    findContour( (90, 200, 100), (140,255,255),
                 frame_HSV, frame, cnv, (255,0,0))
    #findContour( (15, 70, 50), (40,255,255),
    #             frame_HSV, frame,frame, (255,0,0))
    # purple
    findContour( (150, 120, 20), (170,255,255),
                 frame_HSV, frame, cnv, (200,0,100))
    
    cv2.imshow('paint', cnv)
    cv2.imshow('camera', frame)
    #cnv[ cnv > 2 ] -= 2
    cnv[ cnv  > 0  ] -= 1
    key = cv2.waitKey(1)
    #print(key)
    if key == 27:
        break
    if key == 32:
        cnv *= 0
        
    
cv2.destroyAllWindows()
cap.release()
