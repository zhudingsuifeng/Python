#!/usr/bin/env python
#coding=utf-8
#python3.6.5

n=int(input())
zero=0
for i in range(1,n+1):
    zn=0
    t=i
    while t>=5 and i%5==0:  #zero number is related to 5,25,125
        i/=5
        zn+=1
    zero+=zn
print(zero)
        

