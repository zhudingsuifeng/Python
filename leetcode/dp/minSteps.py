#!/usr/bin/env python3
#coding = utf-8

"""
全部复制与黏贴问题，当前位置最小值一定是之前公约数的复制而来
"""

class Solution:
    def mySteps(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[2] = 2
        for i in range(3, n+1):
            for j in range(2, i):
                if i%j == 0:
                    break
            else:
                dp[i] = i
        for i in range(2, n):
            for j in range(2, n//i+1):
                if dp[i*j] == 0:
                    dp[i*j] = dp[i] + j
                else:
                    dp[i*j] = min(dp[i*j], dp[i] + j)
        print(dp)
        return dp[n]

    def minSteps(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(2, n+1):
            for j in range(i//2, 0, -1):
                if i%j == 0:
                    dp[i] = dp[j] + i//j
                    break
        print(dp)
        return dp[n]

if __name__ == "__main__":
    n = int(input())
    s = Solution()
    print(s.minSteps(n))
