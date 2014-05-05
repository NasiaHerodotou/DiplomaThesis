#!/usr/bin/env python

import os
import sys
import subprocess
import csv
from collections import OrderedDict
import time

if __name__ == '__main__':
	classifier=['svm','gmm']
	window=['1','3']
	cmd="rosrun anomaly_detection constant_philosopher.py 10 5 3"
	p1= subprocess.Popen([cmd],shell=True)
	time.sleep(10)
	cmdkill = "rosnode kill constantPhilosopher" 
	pkill= subprocess.call([cmdkill],shell=True)
	#runCmd(cmd)
	for cl in classifier:
			for win in window:
				print "classifier", type(cl)
				print "window", type(win)
				print "trehei o trainer"
				cmdstring = "rosrun anomaly_detection classifier_trainer.py %s %s" % (cl,win)
				print "cmdstring=", cmdstring
				p3= subprocess.call([cmdstring],shell=True)
				cmd4="rosrun anomaly_detection classifier_tester.py"
				print "trehei o tester"
				p4= subprocess.call([cmd4],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
				
				apotelesma= OrderedDict()
				for key, val in csv.reader(open("output.csv")): #fortono to csv me ta apotelesmata tou testing
					apotelesma[key] = val
				print "apotelesma=", apotelesma
				apotelesma.update({'faulty:':i}) #pros8eto ston pinaka ta dio stoiheia
				apotelesma.update({'Telos':'---------------------'})
				name="apotelesmata.csv" #ta filao se ena kainourio csv pou ehei kodiko "a"=append pou apla ka8e fora pros8etei sto telos tou pinaka ta kainouria stoiheia
				w = csv.writer(open(name, "a"))
				for key, val in apotelesma.items():
					w.writerow([key, val])
		


