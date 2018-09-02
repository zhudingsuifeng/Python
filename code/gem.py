#!/usr/bin/env python
#coding=utf-8
#python3.6.5

s=input()
res=l=len(s)
while True:
    for i in range(l):
        t=[]
        for j in 'ABCDE':
            t.append(s.find(j))   #s.find(j) return the j's index in the s
        t.sort()
        res=min(res,t[-1])
        s=s[1:]+s[0]              #string rotate
    print(l-res-1)
    break

