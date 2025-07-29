# import library
import pydobot

position = []

device=pydobot.Dobot("/dev/ttyUSB0")

command = ""
while command != "q": 
    command = input("Enter Command : ")
    if command == "s":
        pose = device.get_pose()
        x = pose.position.x
        y = pose.position.y
        z = pose.position.z
        position.append((x, y, z))


for i in range(len(position)):
    x, y ,z = position[i]
    device.move_to(x, y, z, 0.0)
    if (i+1)%3 == 0:
        device.suck(True)
    elif (i+1)%6 == 1:
        device.suck(False)
    elif i == len(position)-1:
        device.suck(False)
