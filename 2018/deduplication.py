#!/usr/bin/env python3
#coding = utf-8

def repeat(s):
    res = []
    for i in s:
        if i not in res:
            res.append(i)
    return "".join(res)

if __name__ == "__main__":
    s = input()
    print(repeat(s))
