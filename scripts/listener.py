#!/usr/bin/env python
import rospy
from uwbtestrun1.msg import Num
from sensor_msgs.msg import Imu  
def NumCallback(num):
    rospy.loginfo(rospy.get_caller_id() + "I heard %d", num.dis)
       
def IMUCallback(imu):

# To Quadrotor sensor body coordinates
 
    rospy.loginfo(rospy.get_caller_id() + "The w-orientation of quarternion %f", imu.orientation.w)
    rospy.loginfo(rospy.get_caller_id() + "The x-orientation of quarternion %f", imu.orientation.x)
    rospy.loginfo(rospy.get_caller_id() + "The y-orientation of quarternion %f", imu.orientation.y)
    rospy.loginfo(rospy.get_caller_id() + "The z-orientation of quarternion %f", imu.orientation.z)
    
    
    rospy.loginfo(rospy.get_caller_id() + "The angular velocity in x-direction is %f", imu.angular_velocity.x)
    rospy.loginfo(rospy.get_caller_id() + "The angular velocity in y-direction is %f", imu.angular_velocity.y)
    rospy.loginfo(rospy.get_caller_id() + "The angular velocity in z-direction is %f", imu.angular_velocity.z)


# To inertial frame of earth-fixed coordinates
    
    rospy.loginfo(rospy.get_caller_id() + "The linear acceleration in x-direction is %f", imu.linear_acceleration.x)
    rospy.loginfo(rospy.get_caller_id() + "The linear acceleration in y-direction is %f", imu.linear_acceleration.y)
    rospy.loginfo(rospy.get_caller_id() + "The linear acceleration in z-direction is %f", imu.linear_acceleration.z)
       
def listener():
   
       
    rospy.init_node('listener', anonymous=True)
   
    rospy.Subscriber("chatter", Num, NumCallback)
    rospy.Subscriber("/raw_imu", Imu, IMUCallback)
       
    rospy.spin()
   
if __name__ == '__main__':
       listener()

