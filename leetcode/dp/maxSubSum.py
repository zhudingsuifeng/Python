#!/usr/bin/env python3
#coding = utf-8

"""
最大子序和，数组中有正有负
分解为一当前元素结尾的最大子序和，全局最大子序和与局部取最大
"""
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        res = nums[0]           # 初始化，以第一个值结尾的最大子序和就是自身
        s = 0                   # 当前和为0
        for i in nums:
            if s > 0:           # 当前和大于零，可以为后续和做贡献
                s += i
            else:               # 当前和小于零，当前和等与当前值
                s = i
            res = max(res, s)   # 所有局部最大和的最大值，就是全局最大和
        return res

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    s = Solution()
    print(s.maxSubArray(nums))

