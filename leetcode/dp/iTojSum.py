#!/usr/bin/env python3
#coding = utf-8

"""
求数组中i到j之间包含端点的和
dp求出每个位置之前所有值的和，返回dp[j]-dp[i-1]
"""
class NumArray:
    def __init__(self, nums: [int]):
        self.res = nums
        for i in range(1, len(nums)):
            self.res[i] += self.res[i-1]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.res[j]
        else:
            return self.res[j] - self.res[i-1]

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    i, j = map(int, input().split())
    n = NumArray(nums)
    print(n.sumRange(i, j))

