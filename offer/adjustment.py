#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def reOrderArray(self, array):
        l = [ i for i in array if i%2 == 1]
        l += [ j for j in array if j%2 == 0]
        return l

    def reOrder(self, array):
        l = []
        r = []
        for i in array:
            if i%2 == 1:
                l.append(i)
            else:
                r.append(i)
        return l+r

if __name__ == "__main__":
    l = list(map(int, input().split()))
    s = Solution()
    print(s.reOrderArray(l))
