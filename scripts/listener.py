#!/usr/bin/env python
import rospy
from uwbtestrun1.msg import Num
   
def callback(num):
    rospy.loginfo(rospy.get_caller_id() + "I heard %d", num.dis)
       
def listener():
   
       
    rospy.init_node('listener', anonymous=True)
   
    rospy.Subscriber("chatter", Num, callback)
   
       
    rospy.spin()
   
if __name__ == '__main__':
       listener()
