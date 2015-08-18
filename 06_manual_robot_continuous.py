
# 06_manual_robot.py
# Use the arrow keys to direct the robot continuously in the given direction, space to stop

from rrb2 import *
import sys
import tty
import termios

rr = RRB2()
motor_speed = 0.6

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

# These functions allow the program to read your keyboard
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows

# This will control the movement of your robot and display on your screen
print("Use the arrow keys to move the robot and press space to stop")
print("Press CTRL-c to quit the program")

try: 
    while True:
        keyp = readkey()
        if keyp == UP:
            rr.forward()
            print 'forward'
        elif keyp == DOWN:
            rr.reverse()
            print 'backward'
        elif keyp == RIGHT:
            rr.right()
            print 'clockwise'
        elif keyp == LEFT:
            rr.left()
            print 'anti clockwise'
        elif keyp == ' ':
            rr.stop()
            print 'stop'
        elif ord(keyp) == 3:
            break

except KeyboardInterrupt:
    GPIO.cleanup()

