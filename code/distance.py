#!/usr/bin/env python
#coding=utf-8

#python3.6.5

n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

res=2000
for i in range(0,len(x)):
    res=min(res,(x[i]-2+y[i]))

print(res)
