# 07_distance.py
# Uses the ultrasonic rangefinder to measure distance

from rrb2 import *
import time

rr = RRB2()

print("Press CTRL-c to quit the program")

while True:
    dist = rr.get_distance()
    print(dist)
    time.sleep(2)
