#!/usr/bin/env python3
#coding = utf-8

import collections

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        l = sorted(numbers)
        num = l[int(len(l)/2)]
        if l.count(num) > int(len(l)/2):
            return num
        return 0

    def MoreThanHalf(self, numbers):
        tmp = collections.Counter(numbers)
        p = int(len(numbers)/2)
        for num, value in tmp.items():
            if value > p:
                return num
        return 0

if __name__ == "__main__":
    l = list(map(int, input().split()))
    s = Solution()
    print(s.MoreThanHalf(l))
