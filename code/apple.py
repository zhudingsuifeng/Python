#!/usr/bin/env python
#coding=utf-8

#python3.6.5

if __name__=='__main__':
    n=int(input())
    if n%2!=0 or n<6 or n==10:
        print(-1)
    else:
        v=int(n/8)
        if v%8==0:
            print(v)
        else:
            print(v+1)
