# 08_robot_sequence.py
# Moves the robot to attempt a regular polygon shape

from rrb2 import *

rr = RRB2()

motor_speed = 1.0
sides = 3
turn = 1.5

print("Press CTRL-c to quit the program")

rr.forward(sides, motor_speed)
rr.right(turn, motor_speed)

rr.forward(sides, motor_speed)
rr.right(turn, motor_speed)

rr.forward(sides, motor_speed)
rr.right(turn, motor_speed)

rr.forward(sides, motor_speed)
rr.right(turn, motor_speed)

