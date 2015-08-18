# 08_robot_zigzag
# moves the robot along a zigzag line

from rrb2 import *

rr = RRB2()
motor_speed = 0.6

print("Press CTRL-c to quit the program")

rr.forward(4, motor_speed)
rr.right(0.5, motor_speed)
rr.forward(1, motor_speed)
rr.left(0.5, motor_speed)
rr.forward(2, motor_speed)
rr.right(0.5, motor_speed)
rr.forward(2, motor_speed)
rr.left(0.5, motor_speed)
