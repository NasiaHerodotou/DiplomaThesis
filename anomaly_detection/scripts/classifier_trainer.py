#!/usr/bin/env python
import rospy
import sys
from dining_philosopher_communications.msg import hungerMsg
import numpy as np
import csv
from numpy import *
from sklearn import svm
import pickle
from svm_anomaly_classifier import SVMAnomalyClassifier
from gmm_anomaly_classifier import GMMAnomalyClassifier
from anomalyclassifier import AnomalyClassifier


class classifierTrainer():
	def __init__(self,pinakasA,mywidth,classifier_code):
		self.code=classifier_code
		if self.code=="svm":
			classifier=SVMAnomalyClassifier(pinakasA,mywidth)
		elif self.code=="gmm":
			classifier=GMMAnomalyClassifier(pinakasA,mywidth)
		else:
			raiseException("Unrecognized Name")
		if isinstance(classifier,SVMAnomalyClassifier):
			print "einai SVMAnomalyClassifier"
		if isinstance(classifier,AnomalyClassifier):
			print "einai AnomalyClassifier"
		self.width=mywidth
		classifier.trainWithDataset(pinakasA,self.width)
		trained_pickled = open('trained.pkl', 'wb') #apo8ikevei to trained montelo sto data.pkl
		pickle.dump(classifier, trained_pickled, -1)
		sys.exit()

			
	
	
	
	
	
if __name__ == "__main__":
	pinakasA=np.loadtxt(open('/home/nasia/Desktop/svn/trunk/philosophers/mytrainSet.csv','rb')) #fortonei to trainet
	print "forto8ike o pinakas A=", pinakasA
	print "hello=", sys.argv[2]
	mywidth=int(sys.argv[2]) #TO DEFTERO ORISMA EINAI TO PLATOS TOU PARA8IROU
	print "width=", mywidth
	classifier_code=sys.argv[1] #TO PROTO ORISMA EINAI O CLASSIFIER: svm,gmm
	x=classifierTrainer(pinakasA,mywidth,classifier_code)
	exit(1)
