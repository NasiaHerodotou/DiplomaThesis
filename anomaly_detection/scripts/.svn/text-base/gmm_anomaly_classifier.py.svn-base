#!/usr/bin/env python
import rospy
from dining_philosopher_communications.msg import hungerMsg
import numpy as np
import csv
from numpy import *
from sklearn.mixture import GMM
from sklearn import mixture
import pickle
from anomalyclassifier import AnomalyClassifier

class GMMAnomalyClassifier(AnomalyClassifier):
	def __init__(self,pinakasA,mywidth):
		print "GMM classifier!"
		self.percent=0.9  #POSOSTO!!!!!!!!
		self.cf=mixture.GMM(n_components=10, cvtype='full')
		AnomalyClassifier.__init__(self,pinakasA,mywidth)
		
	def trainClassifier(self, convertedDataSet):
		self.trainSet=convertedDataSet
		self.trained=self.cf.fit(self.trainSet)
		print "trained=", self.trained
		self.scored=self.cf.score(self.trainSet) #kano score sto trainset
		self.scored_sorted=np.sort(self.scored)#kano sort ton pinaka me ta scores
		self.scored_sorted=self.scored_sorted[::-1] # reverse
		print "scored=", self.scored
		print "scored sorted=", self.scored_sorted
		self.shape= self.scored_sorted.shape #vrisko tis diastaseis tou gia na do posa elements ehei mesa
		print "elements=", self.shape[0]
		self.thres_position= int(self.percent*self.shape[0]) #to threshold einai sti 8esi pou einai 99,5% ta scores megalitera.vrisko afti ti 8esi
		print "threshold_position=", self.thres_position
		self.threshold=self.scored_sorted[self.thres_position]#vrisko tin timi pou analogei se afti ti 8esi..afto einai to threshold mou
		print "threshold for " + str(self.percent*100) + "% =", self.threshold

	def classifyAnomaly(self,testSample): #pairnei to testSet kai to perna apo ton classifier. epistrefei ena dianisma me pi8anotites
		print "trehei i classifyAnomaly tou GMMtester"
		self.Sample=testSample #to sample einai tis morfis 1 x platos para8irou
		self.results=self.cf.score(self.Sample) #to pernaei apo ton classifier o opoios epistrefei ena pinaka me pi8anotites
		print "diastaseis apotelesmatos tou score:", self.results.shape
		for i in xrange(0,self.results.shape[0]):
			print "result=", self.results[i]
			#~ self.result_counter+=1
			#~ print "plithos paratiriseon= ", self.result_counter
			if self.results[i]<self.threshold: #THRESHOLD
				#self.results[i]=-1 #anomalia
				return True
			else:
				#self.results[i]=1 #normal
				return False
				
