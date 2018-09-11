#!/usr/bin/env python
#coding=utf-8
#python3.6.5
"""
#using deque
from collections import deque

n=int(input())
s=list(map(int,input().split()))
d=deque(s)
res=0
while len(d)>1:
    if d[0]==d[-1]:
        d.pop()
        d.popleft()
    elif d[0]>d[-1]:
        d[-2]+=d[-1]
        d.pop()
        res+=1
    else:
        d[1]+=d[0]
        d.popleft()
        res+=1
"""

#using list 

n=int(input())
l=list(map(int,input().split()))
res=0
while len(l)>1:
    if l[0]==l[-1]:
        l.pop(-1)     #list pop(<-1>) pop last element,pop(0) pop first element
        l.pop(0)
    elif l[0]>l[-1]:
        l[-2]+=l[-1]
        l.pop(-1)
        res+=1
    else:
        l[1]+=l[0]
        d.pop(0)
        res+=1

print(res)
