#!/usr/bin/env python
#coding=utf-8
#python3.6.5

s=input()
if len(s)<=6:
    print(s)
elif len(s)<=14:
    print(s[:6]+' '+s[6:])
else:
    print(s[:6]+' '+s[6:14]+' '+s[14:])
