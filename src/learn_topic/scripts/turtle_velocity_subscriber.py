#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class turtle_pose_subscriber() :
    def __init__(self) :
        rospy.init_node('turtle_pose_subscriber', anonymous=True)
        rospy.Subscriber("/turtle1/pose", Pose, self.poseCallback)

    def poseCallback(self, msg:Pose) :
        rospy.loginfo("Turtle pose: x:%0.3f, z:%0.3f", msg.x, msg.y)

    def run(self) :
        rospy.spin()


if __name__ == '__main__' :
    node = turtle_pose_subscriber()
    node.run()

    