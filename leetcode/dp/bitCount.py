#!/usr/bin/env python3
#coding = utf-8

class Solution:
    # 动态规划方法
    def badBits(self, num: int) -> [int]:
        dp = [0]*(num+1)
        for i in range(num+1):
            for j in range(num):
                if i+2**j <= num and dp[i+2**j] == 0:  # 前面已经存在的一定比后面加出来的小,这个方法复杂度过高
                    dp[i+2**j] = dp[i] + 1
        return dp

    # 字符统计方法
    def myBits(self, num: int) -> [int]:
        res = []
        for i in range(num+1):
            res.append(str(bin(i)).count('1'))
        return res

    def countBits(self, num: int) -> [int]:
        dp = [0]*(num+1)
        for i in range(num+1):
            dp[i] = dp[i>>1] + (i&1)   # 使用移位运算，和位运算速度更快
        return dp

if __name__ == "__main__":
    num = int(input())
    s = Solution()
    # print(s.myBits(num))
    print(s.countBits(num))
