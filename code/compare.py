#!/usr/bin/env python
#coding=utf-8
#python3.6.5

"""
#solution1: it's to slow
def lex(l):
    tl=sorted(l)
    for i in range(len(l)):
        if l[i]!=tl[i]:
            return False
    else:
        return True

def lens(l):
    for i in range(len(l)-1):
        if len(l[i])>len(l[i+1]):
            return False
    else:
        return True
if __name__=="__main__":
    n=int(input())
    l=[] 
    for i in range(n): 
        l.append(input())
    #a=lens(l)
    #b=lex(l)
    a=sorted(l,key=len)
    b=sorted(l)
    if a and b:
        print("both")
    elif a and not b:
        print("lengths")
    elif not a and b:
        print("lexicographically")
    else:
        print("none")
"""
"""
#solution2:it's better
n=int(input())
l=[]
for i in range(n):
    l.append(input())

ls=sorted(l,key=len)   #sorted list by length
ly=sorted(l)

if l==ls and l==ly:    #compare list
    print("both")
elif l==ls:
    print("lengths")
elif l==ly:
    print("lexicographically")
else:
    print("none")
"""
#solution3 :it's fastest
n=int(input())
ls=True
ly=True
s0=input()
for i in range(n-1):
    s=input()
    if ls and s0>s:
        ls=False
    if ly and len(s0)>len(s):
        ly=False
    s0=s
if ls and ly:    #compare list
    print("both")
elif ls:
    print("lengths")
elif ly:
    print("lexicographically")
else:
    print("none")
    

