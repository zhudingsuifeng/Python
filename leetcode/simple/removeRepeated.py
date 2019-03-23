#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        t = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[t]:
                t += 1
                nums[t] = nums[i]
        return t+1

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    s = Solution()
    print(s.removeDuplicates(nums))
