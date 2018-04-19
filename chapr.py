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

strs=raw_input()
print(chapr(strs))
