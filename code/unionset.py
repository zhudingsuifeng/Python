#!/usr/bin/env python
#coding=utf-8
#python3.6.5

n=input()
s1=input().split()
s2=input().split()
s=set(s1+s2)   #set1 | set2 union is worse to set(s1+s2)
print(' '.join(map(str,sorted(s,key=int))))  #sorted s by key=int
