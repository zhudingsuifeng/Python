#!/usr/bin/env python
#coding=utf-8
#python3.6.5

def prime(n):
    for i in range(3,n):
        for j in range(2,int(i**(0.5))+1):
            if i%j==0:
                break   #break jump out of a single layer loop
        else:           #else correspond to for meaning that all num in loog not satisfy the condition
            yield i     #return a iterable object and not jump out of loop
            #break
n=int(input())
p=list(prime(n))        #list convert a iterator to a list
print(p)
res=0
for i in range(0,len(p)):
    for j in range(i,len(p)):
        if p[i]+p[j]==n:
            res+=1

print(res)
