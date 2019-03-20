#!/usr/bin/env python3
#coding = utf-8

"""
爬台阶问题，每次可以爬1个或者2个台阶，则n个台阶有多少种爬法。
最后只能爬一次的时候，一定里最终目的还剩1个或者2个台阶。
即f(n) = f(n-1) + f(n-2)
f(1) = 1
f(2) = 2
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1, 2]
        if n < 3:
            return res[n-1]
        else:
            for i in range(2, n):
                res.append(res[i-1]+res[i-2])   # 注意list越界
            return res[-1]

if __name__ == "__main__":
    n = int(input())
    s = Solution()
    print(s.climbStairs(n))
