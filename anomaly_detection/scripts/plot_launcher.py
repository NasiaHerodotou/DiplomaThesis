#!/usr/bin/env python

import os
import sys
import subprocess
import csv
from collections import OrderedDict
import time
from pylab import *
from PIL import Image

if __name__ == '__main__':
	i=0
	testing_time=int(sys.argv[1]) #o xronos pou 8a pairnei times
	#cmdcounter="rosrun remote_counter RemotePositiveCounter forkcnt 10000"
	#cmdcounter="gnome-terminal -e 'bash -c \"rosrun remote_counter RemotePositiveCounter 'forkcnt' '1000'; exec bash\"'"
	#pcounter= subprocess.Popen([cmdcounter],shell=True)

	while i<=21:
		if i==0:
			cmd="rosrun anomaly_detection normal_philosopher.py 10 5"
			cmdkill = "rosnode kill normalPhilosopher" 
		elif i==1:
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
			
		#cmd0="gnome-terminal -e 'bash -c \"rosrun anomaly_detection plot_the_philosopher.py '10'; exec bash\"'"
		p1= subprocess.Popen([cmd],shell=True)
		cmd0="rosrun anomaly_detection plot_the_philosopher.py 10"
		p0= subprocess.Popen([cmd0],shell=True) #den to kano se allo terminal giati argei na anoi3ei kai hanei tis kanonikes metriseis pou dinei o faulty stin arhi
		time.sleep(testing_time) #o hronos pou 8elo na mazevei times gia to testing
		pkill= subprocess.call([cmdkill],shell=True)
		cmdkill2 = "rosnode kill MyPlotListener"
		pkill2= subprocess.call([cmdkill2],shell=True)
		#cmdkillcounter="rosnode kill forkcntRemotePositiveCounter"
		#pkillcounter=subprocess.call([cmdkillcounter],shell=True)
		time.sleep(15)
		
				
		with open('plot.png', 'rb') as f:
			grafiki= f.read()
		
		#grafiki= Image.open("plot.png").show()
		plotstring = "plothorisallagi"+str(i)+".png"
		print "saving to..", plotstring
		with open(plotstring, 'wb') as f:
			f.write(grafiki)
		#grafiki.save(plotstring)
		
		
		
		i+=1
		
		
		
