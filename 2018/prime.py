#!/usr/bin/env python3
#coding = utf-8

def primeNum(m, n):
    res = 0
    for i in range(m, n+1):
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            res += 1
    return res

def prime(n):
    res = [1]*(n+1)
    for i in range(2, int(n**0.5)+1):
        for j in range(2, n):
            if i*j <= n:
                res[i*j] = 0
            else:
                break
    return sum(res)

if __name__ == "__main__":
    m, n = map(int, input().split())
    # print(primeNum(m, n))
    print(prime(n) - prime(m-1))
