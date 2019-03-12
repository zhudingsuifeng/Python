#!/usr/bin/env python3
#coding = utf-8

def product(l):
    l = list(map(int, l.split()))
    if len(l) < 3:
        return 0
    m, n, x, y, z = 0, 0, 0, 0, 0
    for i in l:
        if i == 0:
            continue
        elif i > m:
            x = n
            n = m
            m = i
        elif i > n:
            x = n
            n = i
        elif i > x:
            x = i
        elif i < z:
            y = z
            z = i
        elif i < y:
            y = i
    return max(m*n*x, m*y*z)

def pro(l):
    l = list(map(int, l.split()))
    if len(l) < 3:
        return 0
    l = sorted(l)
    return max(l[-1]*l[-2]*l[-3], l[-1]*l[0]*l[1])

if __name__ == "__main__":
    l = input()
    print(pro(l))
