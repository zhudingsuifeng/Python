#!/usr/bin/env python
#coding=utf-8

#python3.6.5

def rev(s):
    return int(s[::-1])  #string slicing,inversion

x,y=input().split()
res=rev(str(rev(x)+rev(y)))
print(res)
