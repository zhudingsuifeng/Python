#!/usr/bin/env python3
#coding = utf-8

def judge(n, a):
    if n == 1:
        return 1
    res = 1
    for i in range(1, n):
        if a[i-1] + 1 != a[i]:
            res += 1
    return res

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(judge(n, a))
