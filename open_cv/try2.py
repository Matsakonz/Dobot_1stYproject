import cv2 as cv

img = cv.VideoCapture(0)

while True:
    ret, frame = img.read()
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        img.release()
        cv.destroyAllWindows()
        break
