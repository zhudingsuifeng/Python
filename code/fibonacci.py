#!/usr/bin/env python
#coding=utf-8

#python3.6.5

n=int(input())

i=0
o=1
while o<n:
    t=o
    o=i+o
    i=t
print(min(o-n,n-i))
