import cv2 as cv
import numpy as np

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

    # Break the loop if 'q' is pressed
    if key == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv.destroyAllWindows()
