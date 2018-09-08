#!/usr/bin/env python
#coding=utf-8
#python3.6.5

w,h=map(int,input().split())
if w%4==0 or h%4==0:   #It's a number game.
    print(w*h//2)
elif w%2==0 and h%2==0:
    print((w*h//4+1)*2)
else:
    print(w*h//2+1)
