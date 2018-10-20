#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def Add(self, num1, num2):
        # 列表求和
        return sum([num1, num2])

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    s = Solution()

    print(s.Add(num1, num2))
