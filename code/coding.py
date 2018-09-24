#!/usr/bin/env python3
#coding=utf-8

s=input()
n=len(s)
res=(ord(s[0])-97)*(25**3+25**2+25+1)
if n>1:
    res+=(ord(s[1])-97)*(25**2+25+1)+1
if n>2:
    res+=(ord(s[2])-97)*(25+1)+1
if n>3:
    res+=ord(s[3])-97+1
print(res)
