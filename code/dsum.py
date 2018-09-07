#!/usr/bin/env python
#coding=utf-8
#python3.6.5

from fractions import Fraction
import math

def dec_sum(A,r):
    s=A%r
    if A//r==0:
        return s
    else:
        s+=dec_sum(A//r,r)
        return s

A=int(input())
res=0
for r in range(2,A):
    res+=dec_sum(A,r)
res=Fraction(res,A-2)  #Fraction(a,b) print a/b if denominator is not 1
if res//1==res:
    print(str(res)+'/'+str(1))
else:
    print(res)
