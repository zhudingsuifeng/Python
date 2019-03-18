#!/usr/bin/env python3
#coding = utf-8

def fly(n, s, f):
    res = 0
    for i in f:
        if s >= i:
            res += 1
            s -= i
        else:
            break
    return res

if __name__ == "__main__":
    n, s = map(int, input().split())
    f = list(map(int, input().split()))
    print(fly(n, s, f))
