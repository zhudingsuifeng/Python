#!/usr/bin/env python3
#coding = utf-8

def Len(n, s):
    res = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            res += 1
    return res

if __name__ == "__main__":
    n = int(input())
    s = input().split()
    print(Len(n, s))
