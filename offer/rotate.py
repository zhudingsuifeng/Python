#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        for i in range(0, len(rotateArray) - 1):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]
        else:
            return rotateArray[0]

if __name__ == "__main__":
    l = list(map(int, input().split()))
    s = Solution()
    print(s.minNumberInRotateArray(l))
