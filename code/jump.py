#!/usr/bin/env python3
#coding = utf-8

def jump(n, l):
    res = [0]*n
    l = l[::-1]
    if l[0] == 0:  # init parameter
        res[0] = float('inf')
    else:
        res[0] = 1
    for i in range(1, n):
        if l[i] == 0:
            res[i] = float('inf')
        elif i+1 > l[i]:  # can you jump ashore in one step?
            res[i] = min(res[i-l[i]:i])+1
        else:
            res[i] = 1
    if res[-1] < float('inf'):
        print(res[-1])
    else:
        print(-1)

if __name__ == "__main__":
    n=int(input())
    l=list(map(int,input().split()))

    jump(n, l)
