#!/usr/bin/env python
#coding=utf-8
#python3.6.5

a,b=input().split()
try:
    a=int(a)
    b=int(b)
except:
    print("error")
else:
    print(a+b)
#try:
#except:
#else:
