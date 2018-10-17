#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def replaceSpace(self, s):
        return s.replace(' ','%20')

if __name__ == "__main__":
    s = input()
    a = Solution()
    print(a.replaceSpace(s))
