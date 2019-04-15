#!/usr/bin/env python3
#coding = utf-8

def lk(k):    # 时间复杂度过高
    if k < 3:
        return k
    dp = [0]*k
    dp[0], dp[1] = 1, 2
    for i in range(2, k):
        dp[i] = 2*dp[i-1] + dp[i-2]
    return dp[-1]%32767

def kItem(k):
    maxk = max(k)
    if maxk < 3:
        return [1, 2]
    dp = [0]*maxk
    dp[0], dp[1] = 1, 2
    for i in range(2, maxk):
        dp[i] = 2*dp[i-1] + dp[i-2]
    return dp

if __name__ == "__main__":
    n = int(input())
    k = []
    for i in range(n):
        k.append(int(input()))
    dpk = kItem(k)
    for j in k:
        print(dpk[j-1]%32767)
