#!/usr/bin/env python
#coding=utf-8
#python3.6.5

def conv(m,n):
    t=m
    r=m%n
    res=''
    while t>0:              #all recursions can be implemented in a loop
        r=t%n
        if r<10:
            res+=str(r)
        else:
            res+=chr(r+55)  #convert ascii to char
        t=t//n
    return res

m,n=map(int,input().split())
res=conv(abs(m),n)[::-1]
if m<0:
    print('-'+res)
else:
    print(res)
