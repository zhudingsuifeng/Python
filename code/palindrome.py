#!/usr/bin/env python
#coding=utf-8
#python3.6.5

A=input()
B=input()
res=0
for i in range(0,len(A)+1):
    ab=A[:i]+B+A[i:]  #string insertion
    if ab==ab[::-1]:  #Reverse reading string
        res+=1
print(res)
