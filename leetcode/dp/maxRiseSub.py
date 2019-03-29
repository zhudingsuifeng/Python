#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        dp = [1]*(len(nums))
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    l = list(map(int, input().split()))
    print(s.lengthOfLIS(l))
