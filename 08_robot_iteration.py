# 08_robot_iteration.py
# Moves the robot to attempt a regular polygon shape

from rrb2 import *

rr = RRB2()

motor_speed = 1.0
sides = 3
turn = 1.5
repeat = 3 # Actually repeats this number + 1 

print("Press CTRL-c to quit the program")

for value in range(repeat):
    rr.forward(sides, motor_speed)
    rr.right(turn, motor_speed)

