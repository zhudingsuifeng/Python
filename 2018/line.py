#!/usr/bin/env python3
#coding = utf-8

def line(n):
    if n == 2:
        return 1
    return 2*(n-1)-1


if __name__ == "__main__":
    n = int(input())
    print(line(n))
