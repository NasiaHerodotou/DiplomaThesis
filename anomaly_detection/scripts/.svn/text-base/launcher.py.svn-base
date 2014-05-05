#!/usr/bin/env python

import os
import sys
import subprocess
import csv
from collections import OrderedDict
import time

if __name__ == '__main__':
	testing_time=int(sys.argv[1]) #o xronos pou 8a ginetai to testing
	classifier=['svm', 'gmm']
	window=[1,3,5,7]
	i=0
	while i<=21:
		#print "Process ID of subprocess %s" % p0.pid
		if i==0:
			cmd="rosrun anomaly_detection normal_philosopher.py 10 5"
			cmdkill = "rosnode kill normalPhilosopher" 
		if i==1:
			cmd="rosrun anomaly_detection constant_philosopher.py 10 5 3"
			cmdkill = "rosnode kill constantPhilosopher" 
		elif i==2:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 2"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==3:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 3"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==4:
			cmd="rosrun anomaly_detection negative_philosopher.py 10 5 -6"
			cmdkill = "rosnode kill negativePhilosopher"
		elif i==5:
			cmd="rosrun anomaly_detection empty_philosopher.py 10 5"
			cmdkill = "rosnode kill emptyPhilosopher"
		elif i==6:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 6"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==7:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 7"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==8:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 8"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==9:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 9"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==10:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 10"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==11:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 11"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==12:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 12"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==13:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 13"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==14:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 14"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==15:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 15"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==16:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 16"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==17:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 17"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==18:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 18"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==19:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 19"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==20:
			cmd="rosrun anomaly_detection changed_hunger_philosophers.py 10 5 20"
			cmdkill = "rosnode kill changedHungerPhilosophers"
		elif i==21:
			cmd="rosrun anomaly_detection starving_philosopher.py 10 5"
			cmdkill = "rosnode kill starvingPhilosopher"
		cmd4="rosrun anomaly_detection normal_philosopher.py 6 5"	
		p4= subprocess.Popen([cmd4],shell=True)
		time.sleep(5)
		#cmd0="terminator-terminal -e 'bash -c \"rosrun anomaly_detection imlistening.py 'test' '10'; exec bash\"'"
		cmd0="rosrun anomaly_detection imlistening.py 'test' '6' '10'"
		p0= subprocess.Popen([cmd0],shell=True) #den to kano se allo terminal giati argei na anoi3ei kai hanei tis kanonikes metriseis pou dinei o faulty stin arhi
		p1= subprocess.Popen([cmd],shell=True)
		#~ cmd0="gnome-terminal -e 'bash -c \"rosrun anomaly_detection imlistening.py 'test' '10'; exec bash\"'"
		#~ p0= subprocess.Popen([cmd0],shell=True)
		time.sleep(testing_time) #o hronos pou 8elo na mazevei times gia to testing
		pkill= subprocess.call([cmdkill],shell=True)
		cmdkill2 = "rosnode kill hunger_listener"
		pkill2= subprocess.call([cmdkill2],shell=True)
		cmdkill4="rosnode kill normalPhilosopher"
		pkill4=subprocess.call([cmdkill4],shell=True)
		
		for cl in classifier:
			for win in window:
				cmdstring = "rosrun anomaly_detection classifier_trainer.py %s %s" % (cl,win)
				print "cmdstring=", cmdstring
				p3= subprocess.call([cmdstring],shell=True)
				cmd4="rosrun anomaly_detection classifier_tester.py"
				print "trehei o tester"
				os.system(cmd4)
				#p4= subprocess.call([cmd4],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
				
				apotelesma= OrderedDict()
				for key, val in csv.reader(open("output.csv")): #fortono to csv me ta apotelesmata tou testing
					apotelesma[key] = val
				print "apotelesma=", apotelesma
				apotelesma.update({'faulty: ':' '+str(i)}) #pros8eto ston pinaka ta dio stoiheia
				apotelesma.update({'Telos ':' '+'---------------------'})
				name="apotelesmata.csv" #ta filao se ena kainourio csv pou ehei kodiko "a"=append pou apla ka8e fora pros8etei sto telos tou pinaka ta kainouria stoiheia
				w = csv.writer(open(name, "a"))
				for key, val in apotelesma.items():
					w.writerow([key, val])
		i+=1
		
		
		
		
			
		
		
	
