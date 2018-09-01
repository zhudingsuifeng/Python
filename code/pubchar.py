#!/usr/bin/env python
#coding=utf-8

#python3.6.5

s=input()
c=input()

for each in c:
    s=s.replace(each,'')  #s.replace("xx","x") replace the xx as x in the s

print(s)
