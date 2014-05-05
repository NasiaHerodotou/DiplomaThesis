#!/usr/bin/env python
from my_hunger_listener import MyHungerListener
import sys
import rospy
from dining_philosopher_communications.msg import hungerMsg
import numpy as np
import csv
from numpy import *
import pickle



if __name__ == '__main__':
	counter=len(sys.argv)-2 #to pli8os einai iso me to pli8os ton orismaton -1 
	print "plithos=", counter
	print "sys.argv=", sys.argv[2:] #apla gia na do an ontos evgale ape3o to proto orisma
	wanted_ids=sys.argv[2:] #APO TO DEFTERO ORISMA KAI META DINO TA IDS TON EPI8IMITON FILOSOFON
	print "ids=", wanted_ids
	action=sys.argv[1] #TO PROTO ORISMA EINAI TO ACTION: train, test
	a={} #dimiourgo ena keno dictionary me onoma a
	for i, v in enumerate(wanted_ids): #antistoiho ka8e id me mia 8esi ston pinaka
		a[v]=i
	print "a=",a #ektipono gia na do an ontos dimiourgi8ike to dictionary
	trainSet=np.zeros((0,counter))
	x=MyHungerListener(counter,wanted_ids,a,action)
	
