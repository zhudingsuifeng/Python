#!/usr/bin/env python
#coding=utf-8

#python3.6.5
#recursive is a question
"""
def half(arr,n):
    left=0
    right=len(arr)-1
    mid=arr[len(arr)/2-1]
    while left!=right:
        if arr[left]<mid:
            left+=1
        else:
            temp=arr[right]
            arr[right]=arr[left]
            arr[left]=temp
            right-=1

    if len(arr)>=n/2 and right-left>=n/2:
        print(arr[left])
    else:
        half(arr,n)
"""

l=list(map(int,input().split()))
t=sorted(l)
n=0
v=t[int(len(t)/2)]
for i in t:
    if i==v:
        n+=1
if n>=len(t)/2:
    print(v)
else:
    print("not a number")
