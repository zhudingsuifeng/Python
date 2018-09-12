#!/usr/bin/env python
#coding=utf-8
#python3.6.5

def min_num(l):
    l=sorted(l)
    res=0
    for i in l:
        if i>res+1:
            break
        else:
            res+=i  #The missing numbers are what we need.
    return res+1

n=int(input())
l=list(map(int,input().split()))
print(min_num(l))
