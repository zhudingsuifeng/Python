#!/usr/bin/env python3
#coding = utf-8

def second(n: int, l: [int]) -> int:
    if n < 2:
        return 0
    return sorted(l)[-2]

if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    print(second(n, l))
