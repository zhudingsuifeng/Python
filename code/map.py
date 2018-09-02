#!/usr/bin/env python
#coding =utf-8
#python3.6.5

s=input()
t=input()

def sub(s,t):   #recursive algorithm
    if len(s)<len(t):
        print("No")
    elif len(t)==0:
        print("Yes")
    else:
        if t[0]==s[0]:
            sub(s[1:],t[1:])
        else:
            sub(s[1:],t)
sub(s,t)
