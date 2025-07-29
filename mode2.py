# setup
import json
from pydobot import *
import cv2 as cv
import numpy as np


posi = {}

device = Dobot("/dev/ttyUSB0")
print("Nong are connecting succesfull as USB0 port.")

calibration = input("Do you want o calibration (y/n) : ")

if calibration == "y":
    exec(open("calibration.py").read())

# Read from JSON file
with open('positionvision.json', 'r') as file:
    my_list_as_lists = json.load(file)

# Convert lists back to tuples
x = [tuple(lst) for lst in my_list_as_lists]
home, posiup_l, posimiddle_l, posilow_l, posiup_r, posiup_2r, posimiddle_r, posilow_r = x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]


# Define color ranges for blue, yellow, red, and green in HSV
color_ranges = {
    'Blue': (np.array([100, 150, 100]), np.array([140, 255, 255])),
    'Yellow': (np.array([22, 93, 100]), np.array([35, 255, 255])),
    'Red': (np.array([0, 120, 70]), np.array([10, 255, 255])),
    'Green': (np.array([35, 100, 100]), np.array([85, 255, 255]))
}

# Open a video capture or read an image
cap = cv.VideoCapture(0)  # Change to a file path if using an image or video file

# Initialize a flag to determine when to save data
save_data = False
time = 0
while True:
    # Read a frame from the capture
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Initialize the object counter for each color
    counters = {color: 1 for color in color_ranges}

    # Initialize a list to store positions and colors
    positions_and_colors = []

    for color, (lower, upper) in color_ranges.items():
        # Create a mask for the current color
        mask = cv.inRange(hsv, lower, upper)

        # Find contours in the mask
        contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Calculate the area of each contour
            area = cv.contourArea(contour)
            
            # Filter out contours based on area
            if area < 800 or area > 4000:
                continue
            
            # Get the minimum enclosing rectangle for the contour
            rect = cv.minAreaRect(contour)
            (x, y), (w, h), angle = rect
            
            # Convert values to integers for drawing
            x, y = int(x), int(y)
            w, h = int(w / 2), int(h / 2)
            
            # Draw a circle at the center of the rectangle
            cv.circle(frame, (x, y), 3, [0, 0, 255], -1)
            
            # Draw the bounding rectangle
            box = cv.boxPoints(rect)  # Get the 4 corners of the bounding box
            box = np.int0(box)  # Convert coordinates to integers
            
            # Define color for the bounding box and label
            if color == 'Blue':
                box_color = (255, 0, 0)  # Blue
                label_color = (255, 0, 0)
            elif color == 'Yellow':
                box_color = (0, 255, 255)  # Yellow
                label_color = (0, 255, 255)
            elif color == 'Red':
                box_color = (0, 0, 255)  # Red
                label_color = (0, 0, 255)
            elif color == 'Green':
                box_color = (0, 255, 0)  # Green
                label_color = (0, 255, 0)

            cv.drawContours(frame, [box], 0, box_color, 2)
            
            # Prepare the label text with a unique identifier
            label = f'{color} {counters[color]}'
            
            # Define the position for the label
            label_position = (x - 50, y - 10)  # Adjust the position as needed
            
            # Define font, scale, color, and thickness for the text
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            font_thickness = 1
            
            # Put the text on the image
            cv.putText(frame, label, label_position, font, font_scale, label_color, font_thickness, cv.LINE_AA)
            
            # Save the position and color to the list
            positions_and_colors.append(f'{color} {counters[color]}: ({x}, {y})')
            
            # Increment the counter for the current color
            counters[color] += 1
    time += 1
    if ((time % 50) == 0) and (time <= 200) :
        print(int(time/50)-1)
    # Display the resulting frame
    cv.imshow('Frame', frame)

    # Check for key presses
    key = cv.waitKey(1) & 0xFF
    if time == 200:
        # Save data to a file when 's' is pressed
        with open('positionscam.txt', 'w') as file:  # Open in append mode
            for entry in positions_and_colors:
                file.write(entry + '\n')
        print('Data saved to positions.txt')
        break

    # Break the loop if 'q' is pressed
    if key == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv.destroyAllWindows()


f = open('positionscam.txt', 'r')

for lst in f:
    first, sec = lst.split(":")
    posi[first] = sec.strip()

def checktarget():
    # check target
    if int(y2[:-1]) == int(rup):
        device.move_to(float(posiup_r[0]), float(posiup_r[1]), float(posiup_r[2])-(float(posiup_r[2])*h*0.9)-(15*h), 0.0)
        device.suck(False)
        device.move_to(float(posiup_r[0]), float(posiup_r[1]), float(posiup_r[2])-(float(posiup_r[2])*h*0.9), 0.0)
    elif int(y2[:-1]) == int(r2up):
        device.move_to(float(posiup_2r[0]), float(posiup_2r[1]), float(posiup_2r[2])-(float(posiup_2r[2])*h*0.9)-(15*h), 0.0)
        device.suck(False)
        device.move_to(float(posiup_2r[0]), float(posiup_2r[1]), float(posiup_2r[2])-(float(posiup_2r[2])*h*0.9), 0.0)
    elif int(y2[:-1]) == int(rmiddle):
        device.move_to(float(posimiddle_r[0]), float(posimiddle_r[1]), float(posimiddle_r[2])-(float(posimiddle_r[2])*h*0.9)-(15*h), 0.0)
        device.suck(False)
        device.move_to(float(posimiddle_r[0]), float(posimiddle_r[1]), float(posimiddle_r[2])-(float(posimiddle_r[2])*h*0.9), 0.0)
    elif int(y2[:-1]) == int(rlow):
        device.move_to(float(posilow_r[0]), float(posilow_r[1]), float(posilow_r[2])-(float(posilow_r[2])*h*0.9)-(15*h), 0.0)
        device.suck(False)
        device.move_to(float(posilow_r[0]), float(posilow_r[1]), float(posilow_r[2])-(float(posilow_r[2])*h*0.9), 0.0)
    device.move_to(float(home[0]),float(home[1]),float(home[2])-(float(home[2])*h*0.9),0)
def checkposition(posi):
    check1 = []
    check2 = []
    for key in posi.keys():
        x, y = posi[key].split(",")
        if int(x[1:]) < 300:
            check1.append(int(y[:-1]))
        if int(x[1:]) > 300:
            check2.append(int(y[:-1]))
    check1.sort()
    check2.sort()
    lup, lmiddle, llow = check1[0], check1[1], check1[2]
    rup, r2up, rmiddle, rlow = check2[0], check2[1], check2[2], check2[3]
    return lup, lmiddle, llow, rup, r2up, rmiddle, rlow

lup, lmiddle, llow, rup, r2up, rmiddle, rlow = checkposition(posi)

origin = ""
for key in posi.keys():
    new = key[:-2]
    if origin != new:
        origin = key[:-2]
        originposi = key
    else:
        x1, y1 = posi[key].split(",")
        x2, y2 = posi[originposi].split(",")
        h = int(key[-1])-1
        if int(y1[:-1]) == int(lup):
            device.move_to(float(home[0]),float(home[1]),float(home[2]),0)
            device.move_to(float(posiup_l[0]), float(posiup_l[1]), float(posiup_l[2])+40, 0.0)
            device.suck(True)
            device.move_to(float(posiup_l[0]), float(posiup_l[1]), float(posiup_l[2]), 0.0)
            device.move_to(float(posiup_l[0]), float(posiup_l[1]), float(posiup_l[2])+40, 0.0)
            # check target
            checktarget()

            device.move_to(float(home[0]),float(home[1]),float(home[2]),0)
        elif int(y1[:-1]) == int(lmiddle):
            device.move_to(float(home[0]),float(home[1]),float(home[2]),0)
            device.move_to(float(posimiddle_l[0]), float(posimiddle_l[1]), float(posimiddle_l[2])+40, 0.0)
            device.suck(True)
            device.move_to(float(posimiddle_l[0]), float(posimiddle_l[1]), float(posimiddle_l[2]), 0.0)
            device.move_to(float(posimiddle_l[0]), float(posimiddle_l[1]), float(posimiddle_l[2])+40, 0.0)
            # check target
            checktarget()
            
            device.move_to(float(home[0]),float(home[1]),float(home[2]),0)
        elif int(y1[:-1]) == int(llow):
            device.move_to(float(home[0]),float(home[1]),float(home[2]),0)
            device.move_to(float(posilow_l[0]), float(posilow_l[1]), float(posilow_l[2])+40, 0.0)
            device.suck(True)
            device.move_to(float(posilow_l[0]), float(posilow_l[1]), float(posilow_l[2]), 0.0)
            device.move_to(float(posilow_l[0]), float(posilow_l[1]), float(posilow_l[2])+40, 0.0)
            # check target
            checktarget()
            
            device.move_to(float(home[0]),float(home[1]),float(home[2]),0)

device.close()