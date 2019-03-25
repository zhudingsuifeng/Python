#!/usr/bin/env python3
#coding = utf-8

def find(n, l):
    for i in range(n+1):
        if i not in l:
            return i

def myFind(n, l):
    return n*(n+1)//2 - sum(l)

if __name__ == "__main__":
    t = list(map(int, input().split()))
    n, l = t[0], t[1:]
    print(find(n, l))
