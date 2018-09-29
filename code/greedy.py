#!/usr/bin/env python3
#coding = utf-8

import bisect
# the module for inserting and sorting operations on ordered arrays.
# bisect.bisect_left(list, value) 
# find the location where the value will be inserted but not inserted.
# returns the position to the left of x if x exists in list.

def money(n, m, limit, maxm):
    limit = sorted(limit)
    maxm = sorted(maxm, key = lambda x : x[1], reverse = True)
    # lambda x : x[1] x is a element in iterable object like list, x[1] is key
    res = 0
    while n > 0 and len(maxm) > 0:
        l = bisect.bisect_left(limit, maxm[0][0]) 
        if l < len(limit):
            res += maxm[0][1]
            n -= 1
            limit.pop(l)
        maxm.pop(0)
    print(res)
    # list.pop(index) pop element value with index and return value
    # list.remove(value) remove element in list which value == value

if __name__ == "__main__":
    n, m = map(int, input().split())
    limit = list(map(int, input().split()))
    maxm = []
    
    for i in range(m):
        maxm.append(list(map(int, input().split())))

    money(n, m, limit, maxm)
