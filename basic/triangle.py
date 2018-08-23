#!/usr/bin/env python
#coding=utf-8
"""
Create on Mon Oct 30 21:46:32 2017
@author:fly
Using pca analyze stock data.
"""
import os
import sys
import numpy as np
import math

#get distance of two points
def distance(p1,p2):
    d=np.sqrt(pow((p1[0]-p2[0]),2)+pow((p1[1]-p2[1]),2))
    return d

#
def judgment(p1,p2,p3):
    if distance(p1,p2)<distance(p2,p3)+distance(p1,p3) and distance(p1,p3)<distance(p2,p3)+distance(p1,p2) and distance(p2,p3)<distance(p1,p2)+distance(p1,p3):
	return 1
    else:
	return 0

#
def combinations(iterable,r):
    pool=tuple(iterable)   #tuple() return a tuple 
    n=len(pool)
    if r>n:
	return
    indices=list(range(r))
    yield tuple(pool[i] for i in indices) 
    while True:
	for i in reversed(range(r)):
	    if indices[i]!=i+n-r:
		break
	    else:
		return
	    indices[i]+=1
	    for j in range(i+1,r):
		indices[j]=indices[j-1]+1
	    yield tuple(pool[i] for i in indices)


num=0
points=[]

pnum=input()
if pnum >=3:

    for i in range(0,pnum):
    	line=sys.stdin.readline()
    	p=line.split()
    	x=float(p[0])
    	y=float(p[1])
    	points.append([x,y])

    points=np.array(points)

    for i in range(0,pnum):
    	for j in range(1,pnum):
	    for k in range(2,pnum):
		if i==j or i==k or j==k:
		    continue
		else:
		    print(i,j,k)
	    	    num+=judgment(points[i],points[j],points[k])
		    print(num)
    print(num)
else:
    print("Not enough points")
