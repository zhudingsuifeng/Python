#!/usr/bin/env python
#coding=utf-8
#python3.6.5

print(' '.join(input().split()[::-1]))  #[::-1] could use for iterable objects,not just strings
#char.join() return a string connection with char from list
"""
def rev(s):
    return s[::-1]   #return string reverse
s=list(input().split())  #string slice
t=''
for each in s:
    t=t+rev(each)+' '

print(rev(t).strip())    #remove char on start and end
"""
