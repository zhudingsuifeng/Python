#!/usr/bin/env python
#coding=utf-8
#python3.6.5
#It is inefficient not using queues.
"""
def arr(n):
    for i in range(0,n):
        yield input()

def queue(c):
    if int(c)==1:
        print(c)
    else:
        res=[c]
        for i in range(int(c)-1,0,-1):
            tl=[str(i)]
            tl.extend(res)   #list1.extend(list2) add list2 elements to list1,and don't return anything,but list1 change
            res=[tl[-1]]+tl[:len(tl)-1]
        print(' '.join(res))

n=int(input())
l=list(arr(n))
for c in l:
    queue(c)
"""
from collections import deque  #deque double queue

n=int(input())
l=[]
for i in range(0,n):
    l.append(int(input()))
for i in l:
    d=deque()                  #create a double queue
    for j in range(i,0,-1):
        d.appendleft(str(j))   #append element on left
        d.appendleft(d.pop())  #pop element on right
    print(' '.join(d))

