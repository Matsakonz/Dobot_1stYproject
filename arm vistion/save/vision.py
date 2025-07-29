import cv2 as cv
import numpy as np

cap = cv.VideoCapture(4)

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)




    # lower mask (0-10)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask0 = cv.inRange(hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask1 = cv.inRange(hsv, lower_red, upper_red)

    # join my masks
    mask = mask0+mask1
    
    contour, Herirachy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cn in contour:
        area = cv.contourArea(cn)
        if area < 800 or area > 5000:
            continue
        
        (x,y), (w,h), angle = cv.minAreaRect(cn)
        x, y, w, h = int(x), int(y), int(int(w)/2), int(int(h)/2)

        cv.circle(frame, (x, y), 3, [0, 0, 255], -1)
        cv.rectangle(frame, [x-w,y-h], [x+w,y+h], [0, 255, 0], 2)



        

    cv.imshow("Frame2", frame)
    cv.imshow("Frame", mask)
    if cv.waitKey(1) == ord("q"):
        cap.release()
        cv.destroyAllWindows()
        break