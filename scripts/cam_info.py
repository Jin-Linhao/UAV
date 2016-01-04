#!/usr/bin/env python
import rospy
from svcam.msg import CamInfo

def CamCallback(cam):
	rospy.loginfo(rospy.get_caller_id() + "Width %d", cam.width)
	rospy.loginfo(rospy.get_caller_id() + "Height %d", cam.height)
	rospy.loginfo(rospy.get_caller_id() + "Distortion Parameters %f", cam.D)
	rospy.loginfo(rospy.get_caller_id() + "Rectification Matrix  %f", cam.K)
	rospy.loginfo(rospy.get_caller_id() + "Camera Intrinsic  %f", cam.R)
	rospy.loginfo(rospy.get_caller_id() + "Projection Matrix %f", cam.p)
       

       
def listener():
   
       
	rospy.init_node('listener', anonymous=True)
	   
	rospy.Subscriber("Cam_Info", CamInfo, CamCallback)

	rospy.spin()
	   
if __name__ == '__main__':
       listener()
