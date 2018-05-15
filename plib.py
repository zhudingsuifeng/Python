#!/usr/bin/env python
#coding=utf-8
"""
Create on Tue May 15 10:12:49 2018
@author:fly
python tutorial.
"""
import os
import sys
import numpy as np
import math
from math import pi as PI

#calculate the area of the circle
def CircleArea(r):
	try:
		r=int(r)
		return PI*r*r
	except:
		print('You must give me an integer or float as radius.')

#
def demo(para):
	try:
		para=para.split()
		para=map(float,para)
		avg=sum(para)/len(para)
		g=[i for i in para if i>avg]
		return (avg,)+tuple(g)
	except:
		print('You must give me an integer or float array as input')


if __name__=="__main__":
	s=raw_input()
	#print(CircleArea(s))
	print(demo(s))
	#print(s.split())

	print("success")
