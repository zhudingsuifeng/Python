#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def myTrees(self, n:int) -> int:
        if n == 0 or n == 1:
            return 1
        res = [1, 1] + [0]*(n-1)
        for i in range(2, n+1):
            if i%2 == 0:
                res[i] = 2*sum([res[j]*res[i-j-1] for j in range(i//2)])
            else:
                res[i] = 2*sum([res[j]*res[i-j-1] for j in range(i//2)]) + res[i//2]**2
        return res[-1]
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        print(dp)
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    n = int(input())
    print(s.numTrees(n))
