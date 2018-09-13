#!/usr/bin/env python
#coding=utf-8
#python3.6.5

h=int(input())
x=int(h**(0.5))
if x**2+x<=h:
    print(x)
else:
    print(x-1)

