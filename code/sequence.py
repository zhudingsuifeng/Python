#!/usr/bin/env python
#coding=utf-8
#python3.6.5

def pair(A,n,k):
    if k<0:
        return 0
    if n==1 and k==0:
        return 1
    if n==1:
        return 0
    if n in A:
        i=A.index(n)  #number n in list last
        if i==n-1:  
            return pair(A[:n-1],n-1,k-n+1)  #because of counting number of pairs ,we need return 0,1
        else:
            return pair(A[:i]+A[i+1:],n-1,k-i)
    else:             #number n is not in list 
        res=0
        for j in range(n):
            if A[j]==0:
                A[j]=n
                res+=pair(A,n,k)  #count number of ordered pair if A[j]==0
                A[j]=0
        return res

n,k=map(int,input().split())
A=list(map(int,input().split()))
print(pair(A,n,k))
