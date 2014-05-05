#!/usr/bin/env python
import rospy
import sys
from dining_philosopher_communications.msg import hungerMsg
import numpy as np
import csv
from numpy import *
from sklearn import svm
import pickle
from anomalyclassifier import AnomalyClassifier


class ClassifierTester():
	def __init__(self,pinakasA): 
		x_pickled = open('trained.pkl', 'rb')
		self.classifier=pickle.load(x_pickled)
		print "class of trained object=", self.classifier.__class__.__name__
		self.result_counter=0
		self.anomaly_counter=0
		self.normal_counter=0
		for row in pinakasA:
			print "row pinakaA=", row
			self.testing=self.classifier.isAnomaly(row)
			if self.testing==True:
				self.anomaly_counter+=1
				print "anomaly"
				print "sinolo normal= ", self.normal_counter
				print "sinolo anomalion= ", self.anomaly_counter
			elif self.testing==False:
				self.normal_counter+=1
				print "normal"	
				print "sinolo normal= ", self.normal_counter
				print "sinolo anomalion= ", self.anomaly_counter
		self.classifier.save_the_array()
		self.para8iro=self.classifier.width
		print "kolos=", self.para8iro
		#results1=np.loadtxt(open('/home/nasia/Desktop/svn/trunk/philosophers/myassosSet.csv','rb')) #ksehorizei tin teleftaia stili tou testSet pou periehei tis pragmatikes apantiseis
		self.classifier.evaluateOnTest(self.para8iro)
		
		
		
		
	
	
	
	
	
if __name__ == "__main__":
	print "hello"
	pinakasA=np.loadtxt(open('/home/nasia/Desktop/svn/trunk/philosophers/mytestSet.csv','rb')) #fortonei to testSet
	#results1=np.loadtxt(open('/home/nasia/Desktop/svn/trunk/philosophers/myassosSet.csv','rb')) #ksehorizei tin teleftaia stili tou testSet pou 
	print "forto8ike o pinakas A=", pinakasA
	#print "forto8ikan oi assoi=", results1
	#print "assoi shape=", results1.shape
	x=ClassifierTester(pinakasA)
