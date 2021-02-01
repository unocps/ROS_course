#!/usr/bin/env python

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String

def talker():
#XXXX TODO

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
