#!/usr/bin/env python

import sys
PKG = 'anomaly_detection' # this package name
import roslib; roslib.load_manifest(PKG)
import rospy
#from remote_counter import countingSrv.srv
from remote_counter.srv import countingSrv
import numpy as np
from numpy import *
import time
import random
from random import normalvariate



class forkClass():
	def __init__(self,count,num_forks):
		self.evaluateTestSet=np.zeros((0,1))
		self.n=1
		print "forkClass"
		
		
	def countingSrv_client(self,counter):
		rospy.wait_for_service('/counter/forkcnt')
		try:
			countingService = rospy.ServiceProxy("/counter/forkcnt", countingSrv)
			resp1 = countingService(counter)
			print resp1.ok
			return resp1.ok
		except rospy.ServiceException, e:
			print "Service call failed: %s"%e
	
	def forkCounter(self,counter):
		print "forkcounter"
		if self.countingSrv_client(counter):
			print "True"
			return True
		else:
			rospy.sleep(.05)
			print "false"
			return False
			
	def getForks(self,num_forks):
		print "get forks"
		return self.forkCounter(-num_forks)
		
	def giveForks(self,num_forks):
		print "give forks"
		while not rospy.is_shutdown(): #oso trehei to ros
			if self.forkCounter(num_forks): #an i forkCounter epistrefei true (dld ehei ginei mia allagi ston metriti ton pirounion)
				break #vges apo tin fiveForks
			
	def recalculateHunger(self,philosopherIState,last_hunger_update_,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		print "last hunger update?", last_hunger_update_
		length=rospy.get_time()-last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			print "EATINGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
			hunger_level_*=pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_+=hunger_increase_rate_*seconds
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		#~ self.last_hunger_update_=rospy.get_time()
		print "recalculated_hunger=", hunger_level_
		return hunger_level_
	
		
	def add_to_array(self,newrow):
		self.evaluateTestSet=np.vstack((self.evaluateTestSet,newrow))
		print "value added to array"
		print "evaluate array=", self.evaluateTestSet
		return
		
	def save_the_array(self):
		np.savetxt('myevaluateTestSet.csv', self.evaluateTestSet)
		print "evaluatetestSet created"
		
		
#~ if __name__ == '__main__':
	#~ count=int(sys.argv[1]) 
	#~ num_forks=int(sys.argv[2]) #ta pirounia pou hreiazetai gia na faei
	#~ x=forkClass(count,num_forks)
	#~ #x.countingSrv_client(count)
	#~ x.getForks(count)
