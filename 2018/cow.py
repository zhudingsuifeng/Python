#!/usr/bin/env python3
#coding = utf-8

def cow(n, x):
    if n == 0:
        return x[0]%1000000007
    x = sorted(x)
    res = x[0]
    for i in range(1, n):
        res *= (x[i]-i)
    return res%1000000007

if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    print(cow(n, x))
