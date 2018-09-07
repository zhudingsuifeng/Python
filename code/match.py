#!/usr/bin/env python
#coding=utf-8
#python3.6.5

import re    #regular expression

s=input()
l=re.split('\D+',s)      #max match non-number,and split the string by character
m=max([len(c) for c in l])
for c in l:
    if len(c)==m:
        print(c)
