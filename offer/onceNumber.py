#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def FindNumsAppearOnce(self, array):
        d = {}
        for i in array:
            d[i] = d.get(i, 0) + 1
        res = [ j for j in d if d[j] == 1]
        return res

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    s = Solution()
    print(s.FindNumsAppearOnce(arr))
