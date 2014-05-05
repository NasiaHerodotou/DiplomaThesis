#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

PKG = 'anomaly_detection' # this package name
import roslib; roslib.load_manifest(PKG)
import sys
import rospy
from dining_philosopher_communications.msg import hungerMsg
import numpy as np
from sklearn.mixture import GMM
import csv
from numpy import *
from sklearn import mixture
import pickle


class MyHungerListener: #akouei tin peina ton filosofon
	def __init__(self,counter,wanted_ids,a,action):
		self.trainSet=np.zeros((0,counter))
		self.assosSet=np.zeros((0,counter))
		self.aa=a
		self.my_wanted_ids=wanted_ids
		self.mycounter=counter #counter=o ari8mos ton filosofon pou hrisimopoioume
		self.hungerList=[0]*self.mycounter #o pinakas pou 8a periehei mesa ta hungerLevels olon ton filosofon ka8e defterolepto  !!!!!!AFTO TO METAKINISA EGO
		self.assosList=[0]*self.mycounter
		print "object created"
		self.my_hunger_listener()
		if action=="train":
			np.savetxt('mytrainSet.csv', self.trainSet)
			print "trainSet created"
		elif action=="test":
			np.savetxt('mytestSet.csv', self.trainSet)
			print "testSet created"
			np.savetxt('myassosSet.csv', self.assosSet)
		
			
		
		
	

	def my_update_hunger_list(self,philosopherId, data): #pairnei to id kai to hungerLevel kai to pros8etei sti lista
		rospy.loginfo("Philosopher %d hunger Level= %s",philosopherId, data.hungerLevel)
		position=self.aa[str(philosopherId)] #i 8esi stin opoia 8a mpei i timi tou filosofou antistoihei se mia 8esi pou ehei proka8oristei apo to dictionary
		print "position=", position
		self.hungerList[position]=data.hungerLevel
		print "hunger_list_updated=", self.hungerList
		
	
	def my_update_assos_list(self,philosopherId,data):
		rospy.loginfo("Philosopher %d hunger Level= %s",philosopherId, data.hungerLevel)
		position=self.aa[str(philosopherId)] #i 8esi stin opoia 8a mpei i timi tou filosofou antistoihei se mia 8esi pou ehei proka8oristei apo to dictionary
		print "position=", position
		self.assosList[position]=data.hungerLevel
		print "assos_list_updated=", self.assosList
		
	def my_snapshot_hunger_data(self,event): #pairnei ka8e fora ti hungerList kai tin kanei mia nea grammi ston pinaka pou 8a apotelesei to trainSet
		self.newrow=np.array(self.hungerList) #kanei to hungerList pinaka
		self.newrow2=np.array(self.assosList)
		print "newrow shape=", self.newrow.shape 
		print "trainSet=", self.trainSet
		print "trainSetShape=", self.trainSet.shape
		self.trainSet=np.vstack((self.trainSet,self.newrow)) #pros8etei ti nea grammi sto trainset
		self.assosSet=np.vstack((self.assosSet,self.newrow2))
		print self.trainSet.shape
		print "trainSet=", self.trainSet	
		print "assosSet=", self.assosSet
    
    
	def my_hunger_listener(self):
		# in ROS, nodes are unique named. If two nodes with the same
		# node are launched, the previous one is kicked off. The 
		# anonymous=True flag means that rospy will choose a unique
		# name for our 'talker' node so that multiple talkers can
		# run simultaenously.
		rospy.init_node('hunger_listener')
		rospy.Timer(rospy.Duration(0.5), lambda arg: self.my_snapshot_hunger_data(arg)) #timer opou ka8e miso second kalei tin snapshot_hunger_data
		for i in self.my_wanted_ids:
			topicName="/hungerLevel/"+i
			rospy.Subscriber(topicName, hungerMsg, lambda msg, philosopherId=int(i): self.my_update_hunger_list(philosopherId, msg)) #dimiourgeitai subscriber o opoios pairnei to minima kai to id tou philosopher
		
			topicName2="/assos/"
			rospy.Subscriber(topicName2, hungerMsg, lambda msg, philosopherId=int(i): self.my_update_assos_list(philosopherId, msg))
		rospy.spin() # spin() simply keeps python from exiting until this node is stopped



	
