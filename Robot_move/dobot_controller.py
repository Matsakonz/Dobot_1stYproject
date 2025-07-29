import pygame
from pygame.locals import *
import pydobot
import time

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check if any joystick is connected
if pygame.joystick.get_count() == 0:
    raise Exception("No joystick detected.")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick detected: {joystick.get_name()}")

# Initialize Dobot
# Replace 'COM3' with your Dobot's port, or use the correct IP address if using network connection
dobot = pydobot.Dobot(port='/dev/ttyUSB2')

# Define movement parameters
speed = 5  # Movement speed (change based on your needs)

# Main loop
running = True
# Get the current position of the Dobot
current_position = dobot.get_pose()
x, y, z = current_position.position.x, current_position.position.y, current_position.position.z
new_x = x
new_y = y
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == JOYAXISMOTION:
            x_axis = joystick.get_axis(0)  # Horizontal axis
            y_axis = joystick.get_axis(1)  # Vertical axis
            
            # Convert joystick axis values to movement commands
            y_movement = x_axis * speed
            x_movement = y_axis * speed
            
            
            x_movement += x_movement
            y_movement += y_movement
            # Calculate new position
            new_x += x_movement
            new_y += y_movement
            
            # Send movement commands to Dobot
            print(new_x, new_y, z)
            
            dobot.wait_for_cmd(dobot.move_to(new_x, new_y, z))
            dobot._set_queued_cmd_clear()
            
        elif event.type == JOYBUTTONDOWN:
            # Handle button presses if needed
            pass
        elif event.type == JOYBUTTONUP:
            # Handle button releases if needed
            pass

# Disconnect Dobot and clean up
dobot.disconnect()
pygame.quit()
