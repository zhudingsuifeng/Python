#!/usr/bin/env python
#coding=utf-8
#python3.6.5

def apple(n,l):
    if sum(l)%n!=0:
        return -1
    else:
        a=sum(l)//n
        res=0
        for i in l:
            if (i-a)%2!=0:
                return -1
            elif i>=a:  #take care of the apple where come but not where go 
                res+=(i-a)//2
        return res

n=int(input())
l=list(map(int,input().split()))
print(apple(n,l))

