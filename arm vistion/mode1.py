
# setup
import json
from pydobot import *

device = Dobot("/dev/ttyUSB0")
print("Nong are connecting succesfull as USB0 port.")

text_input = input("Use new pattern press 'n' use default pattern press anything : ")
if text_input == "n":
    position_set = []
    leave = ""
    while leave != "e":
        leave = input("Press 's' to save a position or press 'e' to end position : ")
        if leave == "s" or "d" or "r":
            pose = device.get_pose()  
            pose_array = pose.position.x, pose.position.y, pose.position.z, pose.position.r, leave
            position_set.append(pose_array)

    print("Save new pattern!!")

    my_list_as_lists = [list(t) for t in position_set]
    with open('position.json', 'w') as file:
        json.dump(my_list_as_lists, file)
elif text_input == "c":
    print("Cancel!!")
    exit()

print("Running the pattern...")

# Read from JSON file
with open('position.json', 'r') as file:
    my_list_as_lists = json.load(file)

# Convert lists back to tuples
x = [tuple(lst) for lst in my_list_as_lists]

for loop_po in x:
    if loop_po[4] == "s":
        device.move_to(loop_po[0], loop_po[1], loop_po[2], 0.00)
    elif loop_po[4] == "d":
        device.suck(True)
        device.move_to(loop_po[0], loop_po[1], loop_po[2]+20.00, 0.00)
        device.move_to(loop_po[0], loop_po[1], loop_po[2], 0.00)
        device.move_to(loop_po[0], loop_po[1], loop_po[2]+20.00, 0.00)
    elif loop_po[4] == "r":
        device.move_to(loop_po[0], loop_po[1], loop_po[2]+20.00, 0.00)
        device.move_to(loop_po[0], loop_po[1], loop_po[2], 0.00)
        device.suck(False)
        device.move_to(loop_po[0], loop_po[1], loop_po[2]+20.00, 0.00)

print("End of program!!")

device.close()