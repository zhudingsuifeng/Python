#!/usr/bin/env python
#coding=utf-8
#python3.6.5
import math
n,r=map(int,input().split())

res=n
i=1
while i<r:
    t=math.sqrt(n)
    res+=t
    i+=1
    n=t
print('%.2f' % res)
    
