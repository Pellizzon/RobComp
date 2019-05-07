#! /usr/bin/env python
# -*- coding:utf-8 -*-

#Matheus Pellizzon, Thiago Verardo, Lucas Muchaluat
#Vitor Calcete, Pedro Ramos

import rospy
import math

from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import Empty
from nav_msgs.msg import Odometry

empty_msg = Empty()
topico_odom = "bebop/odom"

x = -1
y = -1
z = -1

x0 = -1
y0 = -1
z0 = -1

first = True

def recebeu_leitura(dado):
    global x
    global y
    global z
    global x0
    global y0
    global z0
    global first

    x = dado.pose.pose.position.x
    y = dado.pose.pose.position.y
    z = dado.pose.pose.position.z

    if first:
        x0 = dado.pose.pose.position.x
        y0 = dado.pose.pose.position.y
        z0 = dado.pose.pose.position.z
        first = False

if __name__=="__main__":

    rospy.init_node("print_odom")
    pub = rospy.Publisher("/bebop/cmd_vel", Twist, queue_size=1)
    takeoff = rospy.Publisher('bebop/takeoff', Empty, queue_size = 1, latch=True)
    landing = rospy.Publisher('bebop/land', Empty, queue_size = 1, latch=True)
    recebe_scan = rospy.Subscriber(topico_odom, Odometry , recebeu_leitura)

    while not rospy.is_shutdown():
        takeoff.publish(empty_msg)
        d = math.sqrt((x - x0) ** 2.0 + (y - y0) ** 2.0 + (z - z0) ** 2.0)

        if d < 6:
             v = 0.2  # Velocidade linear
             vel = Twist(Vector3(v,0,0), Vector3(0,0,0))
             pub.publish(vel)
             rospy.sleep(0.1)
        else:
            vel = Twist(Vector3(0,0,0), Vector3(0,0,0))
            pub.publish(vel)
            rospy.sleep(0.1)
            print(z)
            if z > 1:
                vel = Twist(Vector3(0,0,-.1), Vector3(0,0,0))
                pub.publish(vel)
                rospy.sleep(0.2)
            else:
                landing.publish(empty_msg)
                rospy.sleep(1.0)


