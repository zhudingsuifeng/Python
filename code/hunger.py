#!/usr/bin/env python3
#coding=utf-8

def move(x,mod):
    if x%mod==0:
        return 0
    x=(x*4+3)%mod
    if x==0:
        return 1
    for i in range(3,300002):
        x=(x*2+1)%mod             #4*x+3 等于做了两次2*x+1，8*x+7等玉三次。
        if x==0:
            if i%3==0:
                return i//3
            else:
                return i//3+1
    return -1

if __name__=="__main__":
    x=int(input())
    mod=1000000007
    res=move(x,mod)
    if res>100000:
        print(-1)
    else:
        print(res)
