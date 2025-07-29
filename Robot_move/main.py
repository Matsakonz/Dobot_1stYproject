from serial.tools import list_ports
from pydobot import *

# available_ports = list_ports.comports()
# print(f'available ports: {[x.device for x in available_ports]}')
# port = available_ports[0].device

device = Dobot("/dev/ttyUSB0")
print(f"Nong are connecting succesfull as port.")

pose = device.get_pose()    
x, y, z, r = pose.position.x, pose.position.y, pose.position.z, pose.position.r
print(f"The Nong Position is : [X:{x}, Y:{y}, Z:{z}, R:{r}]")



# device.move_to(x, y, z+50.0, r)
# # box1
# device.suck(True) # suction ON
# device.move_to(x-30.0, y+65.0, z+50.0, r)
# device.move_to(x-30.0, y+65.0, z+25.0, r)
# device.move_to(x-30.0, y+65.0, z+50.0, r)
# device.move_to(x+0.0, y-65.0, z+50.0, r)
# device.move_to(x+0.0, y-65.0, z+25.0, r)
# device.suck(False) # suction OFF
# device.move_to(x+0.0, y-65.0, z+50.0, r)
# #box2
# device.suck(True) # suction ON
# device.move_to(x-15.0, y+95.0, z+50.0, r)
# device.move_to(x-15.0, y+95.0, z+25.0, r)
# device.move_to(x-15.0, y+95.0, z+50.0, r)
# device.move_to(x+35.0, y-80.0, z+50.0, r)
# device.move_to(x+35.0, y-80.0, z+25.0, r)
# device.suck(False) # suction OFF
# device.move_to(x+35.0, y-80.0, z+50.0, r)
# #box3
# device.suck(True) # suction ON
# device.move_to(x+5.0, y+120.0, z+50.0, r)
# device.move_to(x+5.0, y+120.0, z+25.0, r)
# device.move_to(x+5.0, y+120.0, z+50.0, r)
# device.move_to(x+65.0, y-95.0, z+50.0, r)
# device.move_to(x+65.0, y-95.0, z+25.0, r)
# device.suck(False) # suction OFF
# device.move_to(x+65.0, y-95.0, z+50.0, r)

# device.move_to(x, y, z+50.0, r)
# device.move_to(x, y, z, r)



device.close()