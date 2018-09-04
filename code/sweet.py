#!/usr/bin/env python
#coding=utf-8
#python3.6.5

n1,n2,n3,n4=map(int,input().split())
A=(n1+n3)//2
B=(n2+n4)//2
C=n4-B
if A-B==n1 and B-C==n2 and A+B==n3 and B+C==n4:
    print("%d %d %d" % (A,B,C))
else:
    print("No")
