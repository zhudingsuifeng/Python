#!/usr/bin/env python3
#coding = utf-8

def findSub(s):
    for i in range(len(s)):
        sub = s[:i]
        if s.count(sub)*len(sub) == len(s):  # s.count(sub) 统计字符串sub在字符串s中出现的次数
            return sub
    else:
        return "false"

if __name__ == "__main__":
    s = input()
    print(findSub(s))
