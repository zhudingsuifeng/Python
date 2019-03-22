#!/usr/bin/env python3
#coding = utf-8

def triangle(l: [int]) -> int:
    l = sorted(l)
    return min(sum(l), 2*sum(l[:2])-1)
    # 最长的一条边要小于另外两条边的和

if __name__ == "__main__":
    l = list(map(int, input().split()))
    print(triangle(l))
