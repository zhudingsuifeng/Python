#!/usr/bin/env python
#coding=utf-8

#python3.6.5

g=list(map(int,input().split()))
if g[0]>1024 or g[0]<1 or g[1]>1024 or g[1]<1:
    print(-1)
else:
    if g[0]==g[1]:
        print(1)
    else:
        print(0)
