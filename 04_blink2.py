# 04_blink2.py
# This program blinks each LEDs alternately 

import time
from rrb2 import *

rr = RRB2()

print("Press CTRL-c to quit the program")

while True:
    rr.set_led1(1)
    rr.set_led2(0)
    time.sleep(0.5)
    rr.set_led1(0)
    rr.set_led2(1)
    time.sleep(0.5)
