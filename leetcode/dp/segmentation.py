#!/usr/bin/env python3
#coding=utf-8

"""
一个数组是否可以分成和相等的两部分。
首先，看整个数组的和是否为偶数，不是偶数的话不可能分为和相等的两部分。
是偶数的话，需要维护一个0～sum()//2的序列，序列对应i位置为是否可以使用数列中的数组成和为i。
"""
def seg(n, l):
    if sum(l)%2 == 1:
        return False
    m = sum(l)//2
    res = ['false']*(m+1)
    res[0] = 'true'
    for i in l:    # 一定要先遍历给定序列，因为序列中的每一个数至多使用一次
        for j in range(m+1):   # 当前位置为true，加上数组中剩余i对应位置也为true
            if res[j] == 'true' and i+j <= m:  # 需要判定index是否越界1
                res[i+j] = 'true'
    return res[-1]

if __name__ == "__main__":
    n = int(input())
    l = list(map(int,input().split()))
    print(seg(n, l))
