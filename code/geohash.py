#!/usr/bin/env python3
#coding=utf-8

n=int(input())
low=-90
hight=90
res=''
for j in range(6):
    mid=int((low+hight)/2)
    if n<mid:
        res+='0'
        hight=mid
    else:
        res+='1'
        low=mid
print(res)
