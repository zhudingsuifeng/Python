#!/usr/bin/env python3
#coding = utf-8

def myXor(n: int, m: int) -> int:
    return str(bin(n^m)).count('1')

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(myXor(n, m))
