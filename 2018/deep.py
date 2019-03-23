#!/usr/bin/env python3
#coding = utf-8

def deep(s):
    res = 0
    t = 0
    for i in s:
        if i == "(":
            t += 1
        else:
            t -= 1
        res = max(res, t)
    return res

if __name__ == "__main__":
    s = input()
    print(deep(s))
