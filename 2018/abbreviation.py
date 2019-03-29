#!/usr/bin/env python3
#coding = utf-8

def abb(s):
    res = []
    for i in s:
        res.append(i[0])
    return "".join(res)

if __name__ == "__main__":
    # s = input().split()
    # print(abb(s))
    print("".join(map(lambda word: word[0], input().split())))
