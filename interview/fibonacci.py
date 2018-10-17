#!/usr/bin/env python3
#coding = utf-8

class Solution:
    # @classmethod
    def Fibonacci(self,n):
        # starting from 0
        if n < 2:
            return n
        l = [0]*(n+1)
        l[1], l[2] = 1, 1
        for i in range(3, n+1):
            l[i] = l[i-1] + l[i-2]
        return l[-1]

if __name__ == "__main__":
    n = int(input())
    f = Solution()
    print(f.Fibonacci(n))
