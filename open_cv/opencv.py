import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    rgb_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    lower_green = np.array([150,0,0])
    upper_green = np.array([255,100,100])

    mask = cv.inRange(rgb_image, lower_green, upper_green)
    median = cv.medianBlur(mask, 5)
    res = cv.bitwise_and(frame, frame, mask= median)

    M = cv.moments(median)

    try:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    except:
        cX = 0
        cY = 0

    print(f"x = {cX} y = {cY}")
    cv.circle(frame, (cX,cY), 5, (255, 255, 255), -1)
    cv.putText(frame, "centroid", (cX - 25, cY -25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        cap.release()
        cv.destroyAllWindows()
        break

