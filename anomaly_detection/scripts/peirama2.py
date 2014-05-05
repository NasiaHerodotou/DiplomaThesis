#!/usr/bin/env python

import os
import sys
import subprocess
import csv
from collections import OrderedDict
import time
from pylab import *

if __name__ == '__main__':
	i=1
	grafiki=open('plot.png')		
	plotstring = "plot"+str(i)+".png"
	print "saving to..", plotstring
	savefig(plotstring)
