#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def singleNumber(self, nums: [int]) -> [int]:
        n1, n2, diff = 0, 0, 0
        for num in nums:
            diff ^= num      # 获取两个数的异或值
        d = 1
        while d&diff == 0:   # 找到异或值为1的位
            d = d << 1
        for num in nums:
            if num&d:        # 根据这个值为1或者0分成两组
                n1 ^= num
            else:
                n2 ^= num
        return [n1, n2]

if __name__ == "__main__":
    s = Solution()
    nums = list(map(int, input().split()))
    print(s.singleNumber(nums))
