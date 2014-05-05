#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic



	
import rospy
from dining_philosopher_communications.msg import hungerMsg
import sys
from random import randrange
from forkClass import forkClass
import random
from random import normalvariate

class changedHungerPhilosophers():
	def __init__(self,count,num_forks,scenario_code):
		rospy.init_node('changedHungerPhilosophers', anonymous=False)
		self.philosopher=forkClass(topic_code,num_forks)
		self.philosopherIState="ISTATE_NOTHING"
		#pub = rospy.Publisher('/hungerLevel/'+topic_code, hungerMsg)
		self.last_hunger_update_=rospy.get_time()
		self.hunger_level_=random.normalvariate(2.0, 1.0)
		self.allagi=0 #meta apo posous kiklous 8elo na allazei o filosofos simperifora
		self.kikloi=0
		self.scenario_code=scenario_code
		self.assos_value=1
		rospy.Timer(rospy.Duration(0.5), lambda arg: self.post_hunger(arg))
		self.max_eating_time_=3
		self.max_thinking_time_=3
		self.start()
		self.philosopher.save_the_array()
		
	def start(self):
		while not rospy.is_shutdown():
			self.kikloi+=1
			print "kikloi=", self.kikloi
			state=randrange(2)
			print "state=", state
			if state==0:
				philosopherState="STATE_NOTHING"
				print philosopherState
				self.philosopherIState="ISTATE_NOTHING"
				rospy.sleep(0.1)
			elif state==1:
				philosopherState="STATE_ACTIVE"
				print philosopherState
				self.stateActive()
				print "state Active"
				if self.kikloi<=self.allagi:
					self.hunger_level_=self.philosopher.recalculateHunger(self.philosopherIState,self.last_hunger_update_,self.hunger_level_)
				else:
					self.hunger_level_=self.findTheRightRecalculateHunger(self.scenario_code)
				print "recalculate"
				self.last_hunger_update_=rospy.get_time()
				philosopherIState="ISTATE_WAITING"
			else:
				print "state error"
			
				
				
				
	def stateActive(self):
		if self.kikloi<=self.allagi:
			self.hunger_level_=self.philosopher.recalculateHunger(self.philosopherIState,self.last_hunger_update_,self.hunger_level_)
		else:
			self.hunger_level_=self.findTheRightRecalculateHunger(self.scenario_code)
		#self.hunger_level_=self.philosopher.recalculateHunger(self.philosopherIState,self.last_hunger_update_,self.hunger_level_)
		self.last_hunger_update_=rospy.get_time()
		self.philosopherIState="ISTATE_THINKING"
		print "istatethinking?",self.philosopherIState
		self.think()
		self.philosopherIState="ISTATE_WAITING"
		print "istatewaiting?",self.philosopherIState
		self.eat()
		
	def think(self):
		duration=randrange(0,(self.max_thinking_time_*100)/100)
		print "duration=", duration
		rospy.sleep(duration)
		print "sleeping"
		
	def eat(self):
		have_forks=False
		while (not(have_forks) and not rospy.is_shutdown()):
			have_forks=self.philosopher.getForks(num_forks)
		if self.kikloi<=self.allagi:
			self.hunger_level_=self.philosopher.recalculateHunger(self.philosopherIState,self.last_hunger_update_,self.hunger_level_)
		else:
			self.hunger_level_=self.findTheRightRecalculateHunger(self.scenario_code)
		#self.hunger_level_=self.philosopher.recalculateHunger(self.philosopherIState,self.last_hunger_update_,self.hunger_level_)
		self.last_hunger_update_=rospy.get_time()
		self.philosopherIState="ISTATE_EATING"
		print "istateeating?", self.philosopherIState
		duration=randrange(0,(self.max_eating_time_*100)/100)
		rospy.sleep(duration)
		print "my state is:", self.philosopherIState
		if self.kikloi<=self.allagi:
			self.hunger_level_=self.philosopher.recalculateHunger(self.philosopherIState,self.last_hunger_update_,self.hunger_level_)
		else:
			self.hunger_level_=self.findTheRightRecalculateHunger(self.scenario_code)
		#self.hunger_level_=self.philosopher.recalculateHunger(self.philosopherIState,self.last_hunger_update_,self.hunger_level_)
		self.last_hunger_update_=rospy.get_time()
		philosopherIState="ISTATE_WAITING"
		if have_forks==True:
			self.philosopher.giveForks(num_forks)
		
		
			
		
		
		
		
	
	def post_hunger(self,event):
		if self.kikloi<=self.allagi:
			self.hunger_level_=self.philosopher.recalculateHunger(self.philosopherIState,self.last_hunger_update_,self.hunger_level_)
		else:
			self.hunger_level_=self.findTheRightRecalculateHunger(self.scenario_code)
		#self.hunger_level_=self.philosopher.recalculateHunger(self.philosopherIState,self.last_hunger_update_,self.hunger_level_)
		self.last_hunger_update_=rospy.get_time()
		print self.philosopherIState
		pub = rospy.Publisher('/hungerLevel/'+topic_code, hungerMsg)
		pub2=rospy.Publisher('/assos/', hungerMsg)
		msg =float(self.hunger_level_) 
		msg2=float(self.assos_value)
		rospy.loginfo(msg)
		pub.publish(msg)
		pub2.publish(msg2)
		#self.philosopher.add_to_array(self.assos_value)
	
	def findTheRightRecalculateHunger(self,scenario_code):
		print "faulty"
		self.assos_value=-1
		#philosopher.add_to_array(-1)
		if scenario_code==2:
			self.constant_value=self.recalculateHunger2(self.philosopherIState,self.hunger_level_)
		elif scenario_code==3:
			self.constant_value=self.recalculateHunger3(self.philosopherIState,self.hunger_level_)
		elif scenario_code==6:
			self.constant_value=self.recalculateHunger6(self.philosopherIState,self.hunger_level_)
		elif scenario_code==7:
			self.constant_value=self.recalculateHunger7(self.philosopherIState,self.hunger_level_)
		elif scenario_code==8:
			self.constant_value=self.recalculateHunger8(self.philosopherIState,self.hunger_level_)
		elif scenario_code==9:
			self.constant_value=self.recalculateHunger9(self.philosopherIState,self.hunger_level_)
		elif scenario_code==10:
			self.constant_value=self.recalculateHunger10(self.philosopherIState,self.hunger_level_)
		elif scenario_code==11:
			self.constant_value=self.recalculateHunger11(self.philosopherIState,self.hunger_level_)
		elif scenario_code==12:
			self.constant_value=self.recalculateHunger12(self.philosopherIState,self.hunger_level_)
		elif scenario_code==13:
			self.constant_value=self.recalculateHunger13(self.philosopherIState,self.hunger_level_)
		elif scenario_code==14:
			self.constant_value=self.recalculateHunger14(self.philosopherIState,self.hunger_level_)
		elif scenario_code==15:
			self.constant_value=self.recalculateHunger15(self.philosopherIState,self.hunger_level_)
		elif scenario_code==16:
			self.constant_value=self.recalculateHunger16(self.philosopherIState,self.hunger_level_)
		elif scenario_code==17:
			self.constant_value=self.recalculateHunger17(self.philosopherIState,self.hunger_level_)
		elif scenario_code==18:
			self.constant_value=self.recalculateHunger18(self.philosopherIState,self.hunger_level_)
		elif scenario_code==19:
			self.constant_value=self.recalculateHunger19(self.philosopherIState,self.hunger_level_)
		elif scenario_code==20:
			self.constant_value=self.recalculateHunger20(self.philosopherIState,self.hunger_level_)
		else:
			print "wrong scenario code"
		return self.constant_value
		
	def recalculateHunger2(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_+=hunger_increase_rate_*seconds
		else:
			hunger_level_+=hunger_increase_rate_*seconds
			
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger3(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_*=pow(hunger_decrease_ratio_,seconds)
			
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger6(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_+=pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_+=hunger_increase_rate_*seconds
		#~ if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			#~ hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
				
	def recalculateHunger7(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,pow(seconds,2))
			print "this worked"
		else:
			hunger_level_+=hunger_increase_rate_*seconds
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger8(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_+=hunger_increase_rate_*pow(seconds,2)
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
	
	def recalculateHunger9(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_+=hunger_increase_rate_*pow(seconds,3)
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger10(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=2*pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_+=hunger_increase_rate_*seconds
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger11(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_+=2*hunger_increase_rate_*seconds
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger12(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,2*seconds)
			print "eating works"
		else:
			hunger_level_+=hunger_increase_rate_*seconds
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		print "my hunger is=", hunger_level_
		return hunger_level_
		
	def recalculateHunger13(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_=2*hunger_level_+hunger_increase_rate_*seconds
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger14(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,seconds)/2
		else:
			hunger_level_+=hunger_increase_rate_*seconds
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger15(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_+=hunger_increase_rate_*seconds/2
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger16(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,seconds*3)
		else:
			hunger_level_+=hunger_increase_rate_*seconds
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger17(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_+=3*hunger_increase_rate_*seconds
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger18(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_*=pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_=3*hunger_level_+hunger_increase_rate_*seconds
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger19(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_-=hunger_decrease_ratio_*seconds
		else:
			hunger_level_+=hunger_increase_rate_*seconds
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
		
	def recalculateHunger20(self,philosopherIState,hunger_level_):
		hunger_increase_rate_=1
		hunger_decrease_ratio_=0.8
		length=rospy.get_time()-self.last_hunger_update_
		seconds=length
		print "seconds=", seconds
		if philosopherIState=="ISTATE_EATING":
			hunger_level_=hunger_level_*pow(hunger_decrease_ratio_,seconds)
		else:
			hunger_level_=hunger_level_*pow(2*hunger_increase_rate_,seconds)   #2*1^100000=2 dinei panta sta8eri timi
		if (hunger_level_<0): #(hunger_level_<0 or hunger_level != hunger_level_)
			hunger_level_=0
		self.last_hunger_update_=rospy.get_time()
		return hunger_level_
				
        
if __name__ == '__main__':
	topic_code=sys.argv[1] #TO PROTO ORISMA EINAI O KODIKOS TOU TOPIC STO OPOIO POSTAREI
	num_forks=int(sys.argv[2]) #TO DEFTERO ORISMA EINAI ta pirounia pou hreiazetai gia na faei
	scenario_code=int(sys.argv[3]) #TO TRITO ORISMA EINAI o kodikos tou lan8asmenou senariou
	x=changedHungerPhilosophers(topic_code,num_forks,scenario_code)
	
