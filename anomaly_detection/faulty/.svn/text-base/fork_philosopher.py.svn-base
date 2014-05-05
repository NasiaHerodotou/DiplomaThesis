#!/usr/bin/env python

import sys

import rospy
from forkClass import forkClass


class forkPhilosopher():
	def __init__(self,count,num_forks):
		philosopher=forkClass(count,num_forks)
		self.n=1
		while self.n==1:
			rospy.sleep(10.)
			philosopher.getForks(num_forks)
			rospy.sleep(10.)
			philosopher.giveForks(num_forks)
	
if __name__ == '__main__':
	count=int(sys.argv[1]) 
	num_forks=int(sys.argv[2]) #ta pirounia pou hreiazetai gia na faei
	x=forkPhilosopher(count,num_forks)

