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

def combinations(iterable,r):
    pool=tuple(iterable)
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


def compose(inline,n):
    comb=[]
    for i in range(0,n):
	
    if int(inline[1][])<=maxs:
	return comb
    if n>1:
    	return compose(inline,n-1)
    return comb

inline=[]
comb=[]
rows=3
for i in range(0,rows):
    line=sys.stdin.readline()
    inline.append(line.split())
pool[i] for i in indices
maxs=int(inline[0][0])
for i in range(0,len(inline[1])):

    if int(inline[1][i])<=maxs:
	
print(inline)
#points=np.array(points)




print(comb)
