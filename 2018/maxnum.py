#!/usr/bin/env python3
#coding = utf-8

def maxn(n):
    if n%3 == 1:
        return "12"*(n//3)+"1"
    elif n%3 == 2:
        return "21"*(n//3)+"2"
    else:
        return "21"*(n//3)

if __name__ == "__main__":
    n = int(input())
    print(maxn(n))
