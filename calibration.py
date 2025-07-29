# setup
import json
from pydobot import *

device = Dobot("/dev/ttyUSB0")
print("Nong are connecting succesfull as USB0 port.")

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
with open('positionvision.json', 'w') as file:
    json.dump(my_list_as_lists, file)


device.close()