#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This routine will publish to the turtle1/cmd_vel topic, message type geometry_msgs::Twist
import rospy
from geometry_msgs.msg import Twist

class turtle_vel_publisher() :
    def __init__(self) :
        rospy.init_node('turtle_velocity_publisher', anonymous=True)
        self.turtle_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=8)
        self.rate = rospy.Rate(5)
    
    def run(self) :
        while not rospy.is_shutdown():
            # Initialize geometry_msgs::Twist type message
            turtle_vel_msg = Twist()
            turtle_vel_msg.linear.x = 0.4
            turtle_vel_msg.angular.z = -0.6
            # release the news
            self.turtle_vel_pub.publish(turtle_vel_msg)

            rospy.loginfo("linear is :%0.2f m/s, angular is :%0.2f rad/s",
            turtle_vel_msg.linear.x, turtle_vel_msg.angular.z)

            self.rate.sleep()# Delay according to cycle frequency



if __name__ == '__main__' :
    node = turtle_vel_publisher()
    node.run()