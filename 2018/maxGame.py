#!/usr/bin/env python3
#coding = utf-8

def game(x):
    res = []
    for i in x:
        res.append(int("".join(sorted([j for j in i]))))
    return max(res)

if __name__ == "__main__":
    n = int(input())
    x = input().split()
    print(game(x))
