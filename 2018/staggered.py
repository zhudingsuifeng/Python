#!/usr/bin/env python3
#coding = utf-8

def stag(s):
    res = 0
    temp = 1
    for i in range(len(s)-1):
        print(res, temp)
        if s[i] != s[i+1]:
            temp += 1
        else:
            res = max(res, temp)
            temp = 1
    return max(res, temp)

if __name__ == "__main__":
    s = input()
    print(stag(s))
