#!/usr/bin/env python3
#coding = utf-8

class Solution:
    @classmethod
    def ReverseSentence(cls, s):
        l = s.split(' ')
        return ' '.join(l[::-1])


if __name__ == "__main__":
    s = input()

    print(Solution.ReverseSentence(s))
