#!/usr/bin/env python3
#coding = utf-8

def point(n):
    e = int(n**(0.5))
    res = 0
    for i in range(e+1):
        t = (n-i**2)**(0.5)
        if t // 1 == t:
            if i == 0 or t == 0:
                res += 2
            else:
                res += 4
    print(res)

if __name__ == "__main__":
    n = int(input())

    point(n)
