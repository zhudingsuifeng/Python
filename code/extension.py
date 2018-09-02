#!/usr/bin/env python
#coding=utf-8
#python3.6.5

import os

p=input()
'''
p,f=os.path.split(p)
s,e=os.path.splitext(f)
print(e.strip('.'))
'''
i=p.find('.')
if i==-1:
    print("null")
else:
    print(p[i+1:])

