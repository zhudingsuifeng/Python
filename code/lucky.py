#!/usr/bin/env python
#coding=utf-8
#python3.6.5
"""
#Arithmetic operations are faster than type conversions.
def f(x):
    res=0
    for c in x:
        res+=int(c)
    return res

def g(x):
    res=0
    t=bin(int(x))[2:]   #bin() return string '0b101010'
    for c in t:
        res+=int(c)
    return res
"""
def f(x):
    res=0
    while x>0:
        res+=x%10
        x//=10
    return res

def g(x):
    res=bin(x)
    return res.count('1')   #count() count charactor number in string

n=int(input())
res=0
for i in range(1,n+1):
    if g(i)==f(i):
        res+=1
print(res)
