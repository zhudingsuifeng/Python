#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def singleNumber(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            nums[i] = nums[i-1]^nums[i]   # 异或运算，不依赖额外空间完成一些意想不到的效果
        return nums[-1]

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    s = Solution()
    print(s.singleNumber(nums))
