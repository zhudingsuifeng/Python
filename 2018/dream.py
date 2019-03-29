#!/usr/bin/env python3
#coding = utf-8

def dream(n):
    res = 0
    for i in range(n):
        res += int(input())
    return res - n + 1

if __name__ == "__main__":
    n = int(input())
    print(dream(n))
