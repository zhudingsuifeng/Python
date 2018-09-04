#!/usr/bin/env python
#coding=utf-8
#python3.6.5

s=input()
d={}
for e in s:
    if e.isalpha():  #isalpha() string at least one character and all alphabet
                     #isdigit() string only contains numbers
        d[e]=d.get(e,0)+1  #get dict value by key
        if d[e]==3:
            break
print(e)
