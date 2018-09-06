#!/usr/bin/env python
#coding=utf-8 

def alp(s):
    r=0
    res=0
    for e in range(len(s)-1,-1,-1):
        t=(ord(s[e])-97)*26**(r)
        r+=1
        res+=t
    return res

def _2n(n):
    res=[]
    while True:
        c=chr(n%26+97)
        res.append(c)
        if n//26!=0:
            n//=26
        else:
            break
    return ''.join(res[::-1])

a=input()
b=input()
res=_2n(alp(a)+alp(b))
print(res)
