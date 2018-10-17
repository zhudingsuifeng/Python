#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def jumpFloor(self, number):
        if number < 3:
            return number
        l = [0]*(number+1)
        l[1], l[2] = 1, 2
        for i in range(3, number+1):
            l[i] = l[i-1] + l[i-2]
        return l[-1]

if __name__ == "__main__":
    n = int(input())
    j = Solution()
    print(j.jumpFloor(n))
