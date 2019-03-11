#!/usr/bin/env python3
#coding = utf-8

def judge(n, t, a):
    res = n - abs(t - a)
    return res

if __name__ == "__main__":
    n, t, a = map(int, input().split())
    print(judge(n, t, a))
