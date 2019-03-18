#!/usr/bin/env python3
#coding = utf-8

import heapq
import time 

# python 只实现了小顶堆
def value1(s, k):
    t1 = time.time()
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    res = sorted(d.values())
    heapq.heapify(res)
    while k > 0:
        heapq.heapreplace(res, res[0]-1)
        k -= 1
    t2 = time.time()
    print(t2 - t1)
    return sum([heapq.heappop(res)**2 for i in range(len(res))])

def value2(s, k):
    # t1 = time.time()
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    res = sorted([ i for i in d.values()])
    while k > 0:
        res[-1] -= 1
        k -= 1
        res = sorted(res)
    # t2 = time.time()
    # print(t2 - t1)
    return sum([i**2 for i in res])

if __name__ == "__main__":
    s = input()
    k = int(input())
    print(value2(s, k))
    # print(value1(s, k))
