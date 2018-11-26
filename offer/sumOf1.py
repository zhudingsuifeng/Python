#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def NumberOf1(self,n):
        # 1的二进制除了最后一位是1，其他都是0，移位以后与1进行与运算
        # 这样就能统计二进制补码中1的个数
        return sum([(n >> i & 1) for i in range(0,32)])

if __name__ == "__main__":
    n = int(input())
    s = Solution()
    print(s.NumberOf1(n))
