#!/usr/bin/env python3
#coding = utf-8

"""
爬台阶问题，每次可以爬1个或者2个台阶，每个台阶有体力消耗，怎样爬楼梯才能消耗最小。
当前台阶最小的消耗，等于到达前一个台阶的最小消耗与这个台阶的消耗，与前两个台阶的最小值。
"""
class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        res = [0]*(len(cost)+1)
        for i in range(2, len(cost)+1):
            res[i] = min(res[i-1]+cost[i-1], res[i-2]+cost[i-2])
        return res[-1]

if __name__ == "__main__":
    cost = list(map(int, input().split()))
    s = Solution()
    print(s.minCostClimbingStairs(cost))
