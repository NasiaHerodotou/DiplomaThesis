#!/usr/bin/env python
import rospy
from dining_philosopher_communications.msg import hungerMsg
import numpy as np
import csv
from numpy import *
from sklearn import svm
import pickle
from anomalyclassifier import AnomalyClassifier

class SVMAnomalyClassifier(AnomalyClassifier):
	def __init__(self,pinakasA,mywidth):
		self.instance_counter=0
		self.cf=svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
		print "SVM classifier!"
		AnomalyClassifier.__init__(self,pinakasA,mywidth)
		
	def trainClassifier(self,convertedDataSet):
		self.trainSet=convertedDataSet
		self.trained=self.cf.fit(self.trainSet)
		print "SVM trained"
		
	def classifyAnomaly(self,testSample):
		print "trehei i classifyAnomaly tou svm!"
		self.Sample=testSample
		self.instance=self.cf.predict(self.Sample)
		print "sample meta to predict=",self.instance
		self.instance_counter+=1
		print "Sinolo paratiriseon=", self.instance_counter
		return self.instance==-1 #an self.instance==-1 (anomaly) tote return true allios return false
			
	
