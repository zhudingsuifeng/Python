#!/usr/bin/env python3
#coding = utf-8

def daff(m, n):
    res = []
    for i in range(m, n+1):
        t = i
        s = 0
        while t > 0:
            s += (t%10)**3
            t //= 10
        if s == i:
            res.append(i)
    if len(res) == 0:
        print("no")
    else:
        print(' '.join(map(str, res)))

if __name__ == "__main__":
    m, n = map(int, input().split())

    daff(m, n)
