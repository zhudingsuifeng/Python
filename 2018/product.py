#!/usr/bin/env python3
#coding = utf-8

def product(l):
    m, n, x, y, z = l[0], l[0], l[0], l[0], l[0]
    for i in l[1:]:
        if i > m:
            m, n, x = i, m, n
        elif i > n:
            n, x = i, n
        elif i > x:
            x = i
        elif i < z:
            y, z = i, y
        elif i < y:
            y = i
    return max(m*n*x, m*y*z)

def pro(l):
    if len(l) < 3:
        return 0
    l = sorted(l)
    return max(l[-1]*l[-2]*l[-3], l[-1]*l[0]*l[1])

if __name__ == "__main__":
    _ = input()
    l = list(map(int, input().split()))
    print(pro(l))
