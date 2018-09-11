#!/usr/bin/env python
#coding=utf-8
#python3.6.5

n=int(input())
l=list(map(int,input().split()))

m=p=l[0]
for i in l:
    if p<=0:   #be care for p,the sum of numbers before,if p<0,discard all previous numbers.
        p=i
    else:
        p+=i
    if p>m:
        m=p
print(m)
