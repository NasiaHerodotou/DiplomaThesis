#!/usr/bin/env python
from my_hunger_listener import MyHungerListener
import sys
import rospy
from dining_philosopher_communications.msg import hungerMsg
import numpy as np
import csv
from numpy import *
import pickle
from pylab import *

class MyPlotListener: #akouei tin peina ton filosofon
	def __init__(self,wanted_ids):
		self.trainSet=np.zeros((0,2))
		self.my_wanted_ids=wanted_ids
		self.counter=0
		self.hungerList=[0]*2 #o pinakas pou 8a periehei mesa ta hungerLevels olon ton filosofon ka8e defterolepto  !!!!!!AFTO TO METAKINISA EGO
		print "object created"
		self.my_plot_listener()
		np.savetxt('myplotSet.csv', self.trainSet)
		self.plot_the_philosopher()
			
		
	def plot_the_philosopher(self):
		results =np.loadtxt(open('/home/nasia/Desktop/svn/trunk/philosophers/myplotSet.csv','rb'))
		for row in results:
			seconds= row[0]
			print "second:", seconds
			hunger = row[1]
			print "hunger:",hunger

		plt.figure("Time/Hunger")
		plt.xlabel("Time(s)")
		plt.ylabel("Hunger")
		plt.plot(results[:201,0], results[:201,1]) #8elo ta 10 prota defterolepta, o pinakas enimeronetai ka8e miso defterolepto..ara 8elo tis protes 21 seires tou pinaka (20 seires+1 gia to 0)
		grid(True)
		savefig('plotfilosofos10tipos.png')
		show()
		
	def getColumn(self,filename, column):
		return [result[column] for result in results]

	def my_update_hunger_list(self,philosopherId, data): #pairnei to id kai to hungerLevel kai to pros8etei sti lista
		rospy.loginfo("Philosopher %d hunger Level= %s",philosopherId, data.hungerLevel)
		#self.hungerList[0]=self.counter
		self.hungerList[1]=data.hungerLevel
		print "hunger_list_updated=", self.hungerList
		#self.counter+=0.5
		
	def my_snapshot_hunger_data(self,event): #pairnei ka8e fora ti hungerList kai tin kanei mia nea grammi ston pinaka pou 8a apotelesei to trainSet
		self.hungerList[0]=self.counter
		self.newrow=np.array(self.hungerList) #kanei to hungerList pinaka
		print "newrow shape=", self.newrow.shape 
		print "trainSet=", self.trainSet
		print "trainSetShape=", self.trainSet.shape
		self.trainSet=np.vstack((self.trainSet,self.newrow)) #pros8etei ti nea grammi sto trainset
		print self.trainSet.shape
		print "trainSet=", self.trainSet	
		self.counter+=0.5
    
    
	def my_plot_listener(self):
		# in ROS, nodes are unique named. If two nodes with the same
		# node are launched, the previous one is kicked off. The 
		# anonymous=True flag means that rospy will choose a unique
		# name for our 'talker' node so that multiple talkers can
		# run simultaenously.
		rospy.init_node('MyPlotListener')
		rospy.Timer(rospy.Duration(0.5), lambda arg: self.my_snapshot_hunger_data(arg)) #timer opou ka8e 1 second kalei tin snapshot_hunger_data
		topicName="/hungerLevel/"+str(self.my_wanted_ids)
		print "topicName",topicName
		rospy.Subscriber(topicName, hungerMsg, lambda msg, philosopherId=self.my_wanted_ids: self.my_update_hunger_list(philosopherId, msg)) #dimiourgeitai subscriber o opoios pairnei to minima kai to id tou philosopher
		rospy.spin() # spin() simply keeps python from exiting until this node is stopped
        






if __name__ == '__main__':
	topic=int(sys.argv[1])#TO ORISMA EINAI TO TOPIC STO OPOIO POSTAREI O FILOSOFOS
	wanted_ids=topic
	print "ids=", wanted_ids
	trainSet=np.zeros((0,2))
	x=MyPlotListener(wanted_ids)
	

