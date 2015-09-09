#include <string.h>

#include <stdio.h>
#include <errno.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "ssuwb.h"

#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include "uwbtestrun1/Num.h"
#include <std_msgs/Int8.h>

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "uwbtestrun1");
    ros::NodeHandle n;
    ros::Publisher chatter_pub = n.advertise<uwbtestrun1::Num>("chatter", 1000);
    ros::Rate loop_rate(10);

    int count = 0;




    std::stringstream ss;
    uwbtestrun1::Num msg;

    int* dis;
    int nodes[4];//nodesID of each node
    nodes[0]=101;
    nodes[1]=102;
    nodes[2]=105;
    nodes[3]=106;

            if (argc!=3)
            {
                std_msgs::String msg;
                ss <<"error usage: demo /dev/ttyACM0 serial/usb\n"<<count;
                msg.data = ss.str();
                ROS_INFO("%s", msg.data.c_str());

                //chatter_pub.publish(msg);
                exit(0);
            }

            ssUWB(argv[1],argv[2]);


            while(ros::ok())
            {


                int i;
                for (i=0; i<4; i++)
                {

                    msg.dis= uwb(nodes[i]);
                    chatter_pub.publish(msg);
                    ROS_INFO("DIS: %d, ID: %d", msg.dis,nodes[i]);

                }


                ++count;

            }
            return 0;


}



