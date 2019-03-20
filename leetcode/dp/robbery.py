#!/usr/bin/env python3
#coding = utf-8

"""
打劫问题，要求不能连着两家都打劫
状态转移 dp[i] = max(dp[i-1], dp[i-2]+nums[i])
"""
class Solution:
    def rob(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        res = [nums[0], max(nums[0], nums[1])] + [0]*(len(nums)-2)
        for i in range(2, len(nums)):
            res[i] = max(res[i-1], res[i-2] + nums[i])
        return res[-1]

if __name__ == "__main__":
    s = Solution()
    p = list(map(int, input().split()))
    print(s.rob(p))
