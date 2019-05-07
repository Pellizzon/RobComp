#!/usr/bin/env python

# rodar em terminais diferentes: 
# roscore
# rosrun turtlesim turtlesim_node
# rosrun meu_projeto quadrado_turtle.py
import rospy
from geometry_msgs.msg import Twist, Vector3
from math import pi

def move():
    vel = Twist(Vector3(2,0,0), Vector3(0,0,0))
    
    while not rospy.is_shutdown():

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while current_distance < 5:
            pub.publish(vel)
            t1 = rospy.Time.now().to_sec()
            current_distance = vel.linear.x * (t1-t0)

        vel.linear.x = 0
        pub.publish(vel)
        return

def rotate():
  vel = Twist(Vector3(0,0,0), Vector3(0,0,pi/2))

  t0 = rospy.Time.now().to_sec()
  current_angle = 0

  while current_angle <= pi/2:
      pub.publish(vel)
      t1 = rospy.Time.now().to_sec()
      current_angle = vel.angular.z * (t1-t0)

  vel.angular.z = 0
  pub.publish(vel)
  return

if __name__ == '__main__':
    rospy.init_node('quadrado')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    try:
        for i in range(4):
            move()
            rotate()
    except rospy.ROSInterruptException: pass
