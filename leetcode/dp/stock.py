#!/usr/bin/env python3
#coding = utf-8

"""
股票买卖问题，需要先买再卖
问题分解为，第i天之前卖出最大收益等于第i-1天之前卖出最大收益和第i天价格和之前i-1天最低价差的最大值
"""
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if len(prices) == 0:
            return 0
        res = 0
        minprice = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - minprice)
            minprice = min(minprice, prices[i])
        return res

if __name__ == "__main__":
    s = Solution()
    p = list(map(int, input().split()))
    print(s.maxProfit(p))
