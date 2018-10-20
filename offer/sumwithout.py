#!/usr/bin/env python3
#coding = utf-8

class Solution:
    @classmethod
    def Sum_Solution(cls, n):
        return n and cls.Sum_Solution(n-1) + n
    # return n and m # if n == 0 print 0, if n > 0 print m

if __name__ == "__main__":
    n = int(input())
    print(Solution.Sum_Solution(n))
