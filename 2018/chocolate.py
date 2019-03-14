#!/usr/bin/env python3
#coding = utf-8

def selection(n, h, m, w):
    if n == 0 or m == 0:
        return 0
    h = sorted(h)
    w = sorted(w)
    res, i, j = 0, 0, 0
    while i < m and j < n:
        print(w[i], h[j])
        if w[i] >= h[j]:
            res += 1
            j += 1
        i += 1
    return res

if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))
    m = int(input())
    w = list(map(int, input().split()))
    print(selection(n, h, m, w))
