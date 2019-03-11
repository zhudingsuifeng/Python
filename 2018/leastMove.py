#!/usr/bin/env python3
#coding = utf-8

def least(n, l):
    sl = sorted(l)
    res = 0
    for i in range(n):
        if l[i] != sl[i]:
            res += 1
    return res

if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    print(least(n, l))
