#!/usr/bin/env python3
#coding = utf-8

def repeat(x, k):
    return int(x*int(k))

if __name__ == "__main__":
    x1, k1, x2, k2 = input().split()
    n1 = repeat(x1, k1)
    n2 = repeat(x2, k2)
    if n1 == n2:
        print("Equal")
    elif n1 > n2:
        print("Greater")
    else:
        print("Less")
