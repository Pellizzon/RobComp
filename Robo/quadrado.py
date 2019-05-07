#!/usr/bin/env python
# -*- coding:utf-8 -*-
# rodar em terminais diferentes: 
# export TURTLEBOT3_MODEL=burger
# roslaunch turtlebot3_gazebo turtlebot3_world.launch
# rosrun meu_projeto quadrado.py
import rospy
from geometry_msgs.msg import Twist, Vector3
from math import pi

def move():
    v0 = Twist(Vector3(0,0,0), Vector3(0,0,0))
    pub.publish(v0)
    rospy.sleep(.2)
    vel = Twist(Vector3(.25,0,0), Vector3(0,0,0))
    
    while not rospy.is_shutdown():

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while current_distance < 1 and vel.angular.z == 0:
            rospy.sleep(.1)
            pub.publish(vel)
            t1 = rospy.Time.now().to_sec()
            current_distance = vel.linear.x * (t1-t0)

        vel.linear.x = 0
        pub.publish(vel)
        rospy.sleep(1.0)
        return

def rotate():
  v0 = Twist(Vector3(0,0,0), Vector3(0,0,0))
  pub.publish(v0)
  rospy.sleep(.2)
  vel = Twist(Vector3(0,0,0), Vector3(0,0,pi/4))

  t0 = rospy.Time.now().to_sec()
  current_angle = 0

  while current_angle <= pi/2 and vel.linear.x == 0:
      rospy.sleep(.1)
      pub.publish(vel)
      t1 = rospy.Time.now().to_sec()
      current_angle = vel.angular.z * (t1-t0)

  vel.angular.z = 0
  pub.publish(vel)
  rospy.sleep(1.0)
  return

if __name__ == '__main__':
    rospy.init_node('quadrado')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=3)
    try:
    	for i in range(4):
    		move()
    		rotate()
    except rospy.ROSInterruptException: pass
