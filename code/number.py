#!/usr/bin/env python
#coding=utf-8
#python3.6.5

def max_num(l,mn=[]):  #default parameter
    if len(l)<=0:
        return 
    t=l[0]
    for i in l[1:]:
        if i+t>t+i:
            t=i
    mn.append(t)
    l.remove(t)     #remove the first match of a value in the list
    max_num(l,mn)
    return mn

n=int(input())
l=input().split()
print(''.join(max_num(l)))
