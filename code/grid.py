#!/usr/bin/env python
#coding=utf-8
#python3.6.5

#from math import factorial   #factorial
#x,y=map(int,input().split())
#print(factorial(x+y)//factorial(x)//factorial(y))
#This is a mathematical question

def _path(x,y):
    if x==0 or y==0:
        return 1
    else:
        return _path(x-1,y)+_path(x,y-1)

x,y=map(int,input().split())
res=_path(x,y)
print(res)
