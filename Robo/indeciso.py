#! /usr/bin/env python
# -*- coding:utf-8 -*-


import numpy as np

import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

dist = 0
menor = 0
igual = False
c = False

def scaneou(dado):
	global dist
	global menor
	# print("Faixa valida: ", dado.range_min , " - ", dado.range_max )
	# print("Leituras:")
	l = list(dado.ranges)
	#print(np.array(dado.ranges[0]).round(decimals=2))
	dist = l[0]
	#print("Intensities")
	menor = min(l)
	print(menor)
	#print(np.array(dado.intensities).round(decimals=2))

if __name__=="__main__":

	rospy.init_node("le_scan")

	velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3 )
	recebe_scan = rospy.Subscriber("/scan", LaserScan, scaneou)

	while not rospy.is_shutdown():
		
		if dist != menor:
			velocidade = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0.4))
			velocidade_saida.publish(velocidade)
			rospy.sleep(0.1)

		
			velocidade = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
			velocidade_saida.publish(velocidade)

			vel = Twist(Vector3(0.1, 0, 0), Vector3(0, 0, 0))
			velocidade_saida.publish(velocidade)

		# if dist > 1.02:
		# 	velocidade = Twist(Vector3(.1, 0, 0), Vector3(0, 0, 0))
		# 	velocidade_saida.publish(velocidade)
		# elif dist < 1.0:
		# 	velocidade = Twist(Vector3(-.1, 0, 0), Vector3(0, 0, 0))
		# 	velocidade_saida.publish(velocidade) 
		# else:
		# 	velocidade = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
		# 	velocidade_saida.publish(velocidade)
