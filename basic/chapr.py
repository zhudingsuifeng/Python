#!/usr/bin/env python
#coding=utf-8
"""
Create on Mon Oct 30 21:46:32 2017
@author:fly
Using pca analyze stock data.
"""
import os
import sys
from collections import Counter
import numpy as np
import math

#get the three characters with the highest frequency
def chapr(strch):
    strs=Counter(strch)
    result=sorted(strs.items(),key=lambda k:k[1],reverse=True)
    ch=result[0][0]+result[1][0]+result[2][0]
    for i in range(2,len(result)):
    	if result[i][1]==result[i+1][1]:
	    ch+=result[i+1][0]
	else:
	    return ch

#the problem of dressing in different colors
def dress(instr):
    result=[]
    sub=0
    if instr is None or len(instr)==0:
	return 0
    pattern=instr[0]
    result.append(pattern)
    for s in instr[1:]:
	if s==pattern:
	    result[-1]+=s
	else:
	    pattern=s
	    result.append(pattern)
    for each in result:
	if len(each)==1:
	    sub+=0
	else:
	    sub+=len(each)/2
    return sub

strs=raw_input()
#print(chapr(strs))
print(dress(strs))
