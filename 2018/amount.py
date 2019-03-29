#!/usr/bin/env python3
#coding = utf-8

def prime(n):
    if n <= 2:
        return (n&2)
    res = 1
    for i in range(3, n+1):
        for j in range(2, int(i**0.5) +1):
            if i%j == 0:
                break
        else:
            res += 1
    return res

if __name__ == "__main__":
    n = int(input())
    print(prime(n))
