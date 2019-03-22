#!/usr/bin/env python3
#coding = utf-8

def square(l: [int]) -> int:
    l = sorted(l)
    return l[-1] - l[0] + l[-2] -l[1]
    # 正方形四条边的长度一样，最长的边最后一定会变得和最短的边一样长

if __name__ == "__main__":
    l = list(map(int, input().split()))
    print(square(l))
