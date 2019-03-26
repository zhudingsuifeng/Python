#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def myNumber(self, nums: [int]) -> int:
        return (3*sum(set(nums)) - sum(nums))//2

    # 更加直观一点，好理解一点的通用方法
    def singleNumber(self, nums: [int]) -> int:
        n10, n1, mark = 0, 0, 0
        for num in nums:
            n10 ^= n1 & num    # 统计出现次数是否为2次
            n1 ^= num          # 是否为1次
            mark = ~(n10 & n1) # 满3次清零
            n10 &= mark
            n1 &= mark
        return n1              # 出现一次的数字

    def single(self, nums: [int]) -> int:
        n10, n1 = 0, 0
        for num in nums:
            n1 = (n1^num) & ~n10   # 三进制，当10位是1时代表出现两次，再次出现，进位为零
            n10 = (n10^num) & ~n1
        return n1

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    s = Solution()
    # print(s.single(nums))
    print(s.singleNumber(nums))
