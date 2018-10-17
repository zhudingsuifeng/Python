#!/usr/bin/env python3
#coding = utf-8

class Solution:
    # @classmethod
    def Fibonacci(self,n):
        l = [0]*n
        l[0], l[1] = 1, 1
        for i in range(2, n):
            l[i] = l[i-1] + l[i-2]
        return l[-1]

if __name__ == "__main__":
    n = int(input())
    f = Solution()
    print(f.Fibonacci(n))
