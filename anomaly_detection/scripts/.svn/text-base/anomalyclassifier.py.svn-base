#!/usr/bin/env python


import sys
import rospy
from dining_philosopher_communications.msg import hungerMsg
import numpy as np
import csv
from numpy import *
from sklearn import svm
import pickle
from collections import OrderedDict

class AnomalyClassifier():
	def __init__(self,pinakasA,mywidth):
		print "anomaly classifier!"
		self.width=mywidth
		print "para8iro=", self.width
		self.i=0
		self.evaluateResults=np.zeros((0,1))
		self.testarray=np.zeros((0,self.width))
		print "pinakas testSet=", self.testarray
		
		
		

	def isAnomaly(self,row):
		print "trehei i isAnomaly tis AnomalyClassifier!"
		print "row=",row
		self.checkRowShape(row)
		print "i=", self.i
		if self.i==0: #otan einai i proti metrisi
			self.testarray=self.testSet2
			self.i+=1
		elif self.i<self.width: #stis epomenes metriseis vlepei an ehei 3eperastei to platos tou para8irou
			print "yes!"
			self.testarray=np.vstack((self.testarray,self.testSet2)) #an den ehei 3eperastei to para8iro pros8etei stin oura tou ti nea metrisi
			print "teliko testSet=", self.testarray
			print "shape telikou testset=", self.testarray.shape
			self.i+=1
			print "i= ",self.i
			print self.width
		if self.i>=self.width: #an ehei 3eperastei to platos tou para8irou
			self.testarrayT=self.testarray.ravel() #katevazei ton pinaka se mia diastasi
			print "amastrofo=", self.testarrayT
			print "diastaseis anastrofou=", self.testarrayT.shape
			diastasi=self.testarrayT.shape[0]
			self.testarrayT=np.reshape(self.testarrayT,(1,diastasi)) #fernei ton pinaka sti morfi 1 X platos para8irou
			print "i aigia egennisen afko=", self.testarrayT.shape
			print "to afko=", self.testarrayT
			self.result=self.classifyAnomaly(self.testarrayT) #perna to 1 x platos para8irou apo tin classifyAnomaly
			self.testarray=np.delete(self.testarray, (0), axis=0) #diagrafo tin proti grammi tou pinaka gia na dehtei tin epomeni
			print "kainourios pinakas=", self.testarray
			print "shape kainouriou pinaka=", self.testarray.shape
			self.i-=1
			if self.result==0: #edo analoga me to apotelesma apo8ikevei ston pinaka apotelesmaton 1 i -1 gia na mporesei meta na kanei evaluate
				self.add_to_array(1)
			elif self.result==1:
				self.add_to_array(-1)
			else:
				print "save error"
			return self.result #epistrefei to apotelesma tis classifyAnomaly
			
			
			
		
		
	def add_to_array(self,newrow):
		self.evaluateResults=np.vstack((self.evaluateResults,newrow))
		print "value added to array"
		print "evaluate array=", self.evaluateResults
		
	def save_the_array(self):
		np.savetxt('myevaluateResults.csv', self.evaluateResults)
		print "evaluateResults created"
			
	def trainClassifier(self,convertedDataSet):
		raise NotImplementedError 
		
	def checkRowShape(self,row):
		print "trehei i checkRowShape"
		print "row=", row
		print "shape of row=", row.shape
		self.testSet=row
		if row.shape==(): #se periptosi pou ehoume 1 filosofo i proti grammi dinei 1 monadiko stoiheio to opoio ehei shape ()
			print "nasia rules!"
			self.B=np.reshape(row,(1,1))
			self.testSet=self.B
			print "testSet shape=", self.testSet.shape
			self.shape=10
		else:
			self.shape=row.shape[0] #mege8os protis diastasis
			 
			
			
		if row.shape==(self.shape,): #ama leitourgoun polloi filosofoi i proti grammi tou pinaka dinei element me shape (ari8mos filosofon,)
			self.B=np.reshape(row,(self.shape,1))
			self.testSet=self.B
		
		print "testSet=", self.testSet
		print "testSet shape=", self.testSet.shape
		self.testSet2=self.testSet.T #to antistrefo giati gia kapoio periergo logo den doulevei diaforetika
		print "testSet2=", self.testSet2.shape
		
			
	def trainWithDataset(self,pinakasA,width):
		print "trehei i trainWithSet tis AnomalyClassifier!"
		self.pinakas=pinakasA
		self.width=width
		print "A=", self.pinakas
		print "megalo shape=", self.pinakas.shape      
		stepsize=1
		n=self.pinakas.shape[0]
		if self.pinakas.shape==(n,):
			self.pinakas=np.reshape(self.pinakas,(n,1))
		print "kainourio shape pinaka=",self.pinakas.shape
		A=np.hstack(self.pinakas[i:1+n+i-self.width:stepsize] for i in range(0,self.width) )
		print "pinakas meta to para8iro", A
		mytrainSet=A
		print "mege8os protis diastasis=", A.shape[0]
		shape=A.shape[0] #mege8os protis diastasis
		if A.shape==(shape,): #ama leitourgei mono enas filosofos prepei na ginei reshape o pinakas gia na doule4oun oi ta3inomites
			B=np.reshape(A,(shape,1))
			mytrainSet=B
		print mytrainSet.shape
		self.convertedDataSet=mytrainSet
		self.trainClassifier(self.convertedDataSet)
		
	def classifyAnomaly(self,testSet2):
		raise NotImplementedError
		
	def evaluateOnTest(self,para8iro):
		self.normal=0
		self.anomaly=0
		self.diafonia=0
		self.simfonia=0
		self.anomaly_precision=0
		self.normal_precision=0
		self.actual_anomaly=0
		self.actual_normal=0
		self.true_positives=0
		self.true_negatives=0
		self.false_positives=0
		self.false_negatives=0
		results1=np.loadtxt(open('/home/nasia/Desktop/svn/trunk/philosophers/myassosSet.csv','rb')) #ksehorizei tin teleftaia stili tou testSet pou periehei tis pragmatikes apantiseis
		print "print=", results1
		print "results1 shape=", results1.shape
		if results1.shape==(results1.shape[0],):
			self.results=results1
		else:
			self.results=results1[:,-1] #an eho parapano filosofous pairno tin teleftaia stili pou einai o faulty
		print "para8iro=", para8iro
		if para8iro>1:
			step=para8iro-1
			print "step=", step #an eho para8iro prepei na afaireso (para8iro-1) seires apo to telos gia na simfonoun oi assoi
			i=0
			while i<step:
				self.results=np.delete(self.results, (0),axis=0) 
				i+=1
			print "self.results=", self.results
		print "afta pou edose o filosofos(results)", self.results
		self.test_model=self.evaluateResults #apo8ikevei stin test_model to ekpaidevmeno testSet (dld to dianisma me ta 1 kai -1)
		print "afta pou edose to classification (evaluateResults)", self.test_model
		for i in xrange(0,self.test_model.shape[0]): #apo to 0 mehri to mege8os tis protis diastasis tou test_model
			if self.test_model[i]==-1: #an to test_model ehei anomalia (tou classifier)
				self.anomaly+=1        #pros8eto 1 stis anomalies
				if self.results[i]==-1: # an kai sta pragmatika apotelesmata tou testSet iparhei episis anomalia
					self.anomaly_precision+=1 #af3ano to anomaly_precision (nomizo den hreiazetai kan)
					self.simfonia+=1
					self.true_positives+=1 #einai pragmatiki anomalia kai o algori8mos to ekane classify san anomalia
				else:
					self.diafonia+=1
					self.false_positives+=1 #einai pragmatika normal alla o algori8mos to ekane classify san anomalia
			else:
				self.normal+=1 #allios pros8eto 1 sta normal (normal tou classifier)
				if self.results[i]==1: #an kai sta pragmatika apotelesmata einai normal
					self.normal_precision+=1 #pros8eto 1 sto normal_precision (kai pali nomizo oti den hreiazetai)
					self.simfonia+=1
					self.true_negatives+=1 #o algori8mos to vrike normal kai einai ontos normal
				else:
					self.diafonia+=1
					self.false_negatives+=1 #o algori8mos to vrike normal eno stin pragmatikotita einai anomalia
	
	
		for i in xrange(0,self.results.shape[0]):
			if self.results[i]==-1: #metrao oles tis pragmatikes anomalies
				self.actual_anomaly+=1
			else:
				self.actual_normal+=1 #metrao ola ta pragmatika normal
		print "oi pragmatikes anomalies einai:", self.actual_anomaly
		print "ta pragmatika normal apotelesmata einai:", self.actual_normal
		print "oi ipologismenes apo to svm anomalies einai:", self.anomaly
		print "oi ipologismenes apo to svm normal einai:", self.normal 
		print "ta sinolika apotelesmata einai:", len(self.results)
		print "ta apotelesmata pou simfonoun einai:", self.simfonia
		print "ta apotelesmata pou diafonoun einai:", self.diafonia
		if self.true_positives+self.false_negatives!=0:
			self.anomaly_recall=self.true_positives/float(self.true_positives+self.false_negatives)
		else:
			self.anomaly_recall="-"
		print "Anomaly recall(poses fores apo oses einai pragmatika anomalia to vriskei- (tp/(tp+fn))="
		print self.anomaly_recall
		if self.true_positives+self.true_negatives+self.false_positives+self.false_negatives!=0:
			self.accuracy=(self.true_positives+self.true_negatives)/float(self.true_positives+self.true_negatives+self.false_positives+self.false_negatives)
		else:
			self.accuracy="-"
		print "Accuracy (periptoseis pou simfonoun/to sinolo ton apotelesmaton-(tp+tn)/(tp+tn+fp+fn)="
		print self.accuracy
		if self.true_positives+self.false_positives!=0:
			self.final_anomaly_precision= self.true_positives/float(self.true_positives+self.false_positives)
		else:
			self.final_anomaly_precision="-"
		print "Anomaly precision (poses apo tis fores pou 8eorei kati anomalia, einai ontos pragmatika anomalia-tp/(tp+fp))="
		print self.final_anomaly_precision
		self.a8roisma=float(self.true_positives+self.true_negatives+self.false_positives+self.false_negatives)
		print "tp+tn+fp+fn=", self.a8roisma
		#~ self.apotelesmata=OrderedDict([('Classifier: ',self.__class__.__name__),
		#~ ('Window: ',self.width),
		#~ ('True_Positives: ',self.true_positives),
		#~ ('True_Negatives: ',self.true_negatives),
		#~ ('False_positives: ',self.false_positives),
		#~ ('False_negatives: ',self.false_negatives),
		#~ ('tp+tn+fp+fn= ',self.a8roisma),
		#~ ('Anomaly_Recall: ',self.anomaly_recall),
		#~ ('Accuracy: ',self.accuracy),
		#~ ('Anomaly_Precision: ',self.final_anomaly_precision)])
		
		self.apotelesmata=OrderedDict()
		self.apotelesmata['Classifier: '] =' '+self.__class__.__name__
		self.apotelesmata['Window: ']=' '+str(self.width)
		self.apotelesmata['True_Positives(tp): ']=' '+str(self.true_positives)
		self.apotelesmata['True_Negatives(tn): ']=' '+str(self.true_negatives)
		self.apotelesmata['False_positives(fp): ']=' '+str(self.false_positives)
		self.apotelesmata['False_negatives(fn): ']=' '+str(self.false_negatives)
		self.apotelesmata['tp+tn+fp+fn= ']=' '+str(self.a8roisma)
		self.apotelesmata['Anomaly_Recall: ']=' '+str(self.anomaly_recall)
		self.apotelesmata['Accuracy: ']=' '+str(self.accuracy)
		self.apotelesmata['Anomaly_Precision: ']=' '+str(self.final_anomaly_precision)
		print "Apotelesmata=",self.apotelesmata
		name="output.csv"
		w = csv.writer(open(name, "w"))
		for key, val in self.apotelesmata.items():
			w.writerow([key, val])
		print "output.csv created"
		#~ apotelesma= OrderedDict()
		#~ for key, val in csv.reader(open("output.csv")):
			#~ apotelesma[key] = val
		#~ print "apotelesma=", apotelesma
		#~ apotelesma.update({'faulty:':'1'})
		#~ apotelesma.update({'Telos':'---------------------'})
		#~ print "neo apotelesma=", apotelesma
		

		
		
			
