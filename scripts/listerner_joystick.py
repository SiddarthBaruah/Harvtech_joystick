#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy

def joy_callback(data):
    axes = data.axes
    buttons = data.buttons

    # Process the joystick input here
    print("Axes: ", axes)
    print("Buttons: ", buttons)

def joy_listener():
    rospy.init_node('joy_listener', anonymous=True)
    rospy.Subscriber("joy", Joy, joy_callback)
    rospy.spin()

if __name__ == '__main__':
    joy_listener()