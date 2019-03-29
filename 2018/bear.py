#!/usr/bin/env python3
#coding = utf-8

def eatSugar(n: int, m: int, sugar: [int], bear: {}):
    sugar = sorted(sugar, reverse = True)
    for item in sorted(bear.items(), key = lambda x: x[1], reverse = True):
        for i in range(m):
            if item[1][1] >= sugar[i]:
                item[1][1] -= sugar[i]
                sugar[i] = 0
    for i in range(n):
        print(bear[i][1])

if __name__ == "__main__":
    n, m = map(int, input().split())
    sugar = list(map(int, input().split()))
    bear = {}
    for i in range(n):
        k, v = map(int, input().split())
        bear[i] = [k, v]    # 熊需要有序
    eatSugar(n, m, sugar, bear)
