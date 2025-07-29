import cv2 as cv
import numpy as np

cap = cv.VideoCapture(4)

while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)




    # lower mask (0-10)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    maskred0 = cv.inRange(hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    maskred1 = cv.inRange(hsv, lower_red, upper_red)

    # join my masks
    mask = maskred0+maskred1
    
    contour, Herirachy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cn in contour:
        area = cv.contourArea(cn)
        if area < 800 or area > 5000:
            continue
        
        (x,y), (w,h), angle = cv.minAreaRect(cn)
        x, y, w, h = int(x), int(y), int(int(w)/2), int(int(h)/2)

        cv.circle(frame, (x, y), 3, [0, 0, 255], -1)
        cv.rectangle(frame, [x-w,y-h], [x+w,y+h], [0, 255, 0], 2)



        

# lower mask (0-10)
    lower_blue = np.array([35, 140, 60]) 
    upper_blue = np.array([255, 255, 180])
    maskblue = cv.inRange(hsv, lower_blue, upper_blue)


    # join my masks
    mask = maskblue
    
    contour, Herirachy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cn in contour:
        area = cv.contourArea(cn)
        if area < 800 or area > 5000:
            continue
        
        (x,y), (w,h), angle = cv.minAreaRect(cn)
        x, y, w, h = int(x), int(y), int(int(w)/2), int(int(h)/2)

        cv.circle(frame, (x, y), 3, [0, 0, 255], -1)
        cv.rectangle(frame, [x-w,y-h], [x+w,y+h], [0, 255, 0], 2)





# lower mask (0-10)
    lower_yellow = np.array([22, 93, 0]) 
    upper_yellow = np.array([45, 255, 255])
    maskyellow = cv.inRange(hsv, lower_yellow, upper_yellow)


    # join my masks
    mask = maskyellow
    
    contour, Herirachy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cn in contour:
        area = cv.contourArea(cn)
        if area < 800 or area > 5000:
            continue
        
        (x,y), (w,h), angle = cv.minAreaRect(cn)
        x, y, w, h = int(x), int(y), int(int(w)/2), int(int(h)/2)

        cv.circle(frame, (x, y), 3, [0, 0, 255], -1)
        cv.rectangle(frame, [x-w,y-h], [x+w,y+h], [0, 255, 0], 2)





# lower mask (0-10)
    lower_green = np.array([50, 100,100]) 
    upper_green = np.array([45, 255, 255])
    maskgreen = cv.inRange(hsv, lower_green, upper_green)


    # join my masks
    mask = maskgreen
    
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
    if cv.waitKey(1) == ord("q"):
        cap.release()
        cv.destroyAllWindows()
        break