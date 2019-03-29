#!/usr/bin/env python3
#coding = utf-8

def maxSum(l):
    if len(l) == 1:
        return l[0]
    dp = l[:]
    for i in range(1, len(l)):
        dp[i] = max(dp[i-1]+l[i], l[i])
    return max(dp)

if __name__ == "__main__":
    l = list(map(int, input().split()))
    print(maxSum(l))
