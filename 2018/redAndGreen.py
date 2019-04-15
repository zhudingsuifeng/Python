#!/usr/bin/env python3
#coding = utf-8

def RG(s):
    res = []
    for i in range(len(s)+1):
        t = 0
        for j in range(len(s)):
            if j <= i and s[j] == 'G':
                t += 1
            if j > i and s[j] == 'R':
                t += 1
        res.append(t)
    return min(res)

def RedAndGreen(s):
    # 还是这种写法更简洁，使用匿名函数和count统计字符个数
    return min(map(lambda i: s[:i].count('G') + s[i:].count('R'), range(len(s)+1)))

if __name__ == "__main__":
    s = input()
    print(RG(s))
