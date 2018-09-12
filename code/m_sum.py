#!/usr/bin/env python
#coding=utf-8
#python3.6.5

def n_m(n,m,s=1,l=[]):
    if m<=0:
        print(' '.join(map(str,l))) 
    for i in range(s,n+1):
        if i>m:
            break
        l.append(i)
        n_m(n,m-i,i+1,l)  #n is number ,s is the smallest number where we start
        l.pop()   #pop i 

n,m=map(int,input().split())
n_m(n,m)
