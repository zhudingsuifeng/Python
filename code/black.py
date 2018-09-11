#!/usr/bin/env python
#coding=utf-8
#python3

n=int(input())
res=[0]*(n+1)
res[1]=3
res[2]=9
for i in range(3,n+1):
    res[i]=2*res[i-1]+res[i-2]  #we need to know the relations of res[i],res[i-1] and res[i-2]

print(res[n])
