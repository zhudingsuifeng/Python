#!/usr/bin/env python3
#coding = utf-8

def maxnum(s, n):
    while n > 0:
        for i in range(1,len(s)):
            if s[i-1] < s[i]:
                s = s[:i-1]+s[i:]
                n -= 1
                break
        else:
            s = s[:-n]
            n = 0
    return s

def number(s, n):
    t = 0
    while t < len(s)-1 and n > 0:
        if s[t] < s[t+1]:
            s = s[:t] + s[t+1:]
            t = t-1 if t >= 1 else 0
            n -= 1
        else:
            t += 1
    if n > 0:
        s = s[:-n]
    return s

if __name__ == "__main__":
    s = input()
    n = int(input())

    print(number(s, n))
