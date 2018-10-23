#!/usr/bin/env python3
#coding = utf-8

import heapq

def sortk(l, k):
    if l is None:
        return None
    if len(l) < k:
        return []
    l = sorted(l)
    return l[:k]

# python中对堆这种结构进行了模块化，可以通过调用heapq来使用堆这种数据结构。
# h = [] # build an empty heap
# heappush(h, item)  # insert an item to heap h
# item = heappop(h)  # pop the smallest element
# heapify(l)         # transform list to heap
# item = heapreplace(h, item) 
# heappushpop()
# merge(*iterables)  # merge the heaps and output heap

def heapk(l, k):
    if not l or not k or len(l) < k:
        return []
    heapq.heapify(l)
    return [heapq.heappop(l) for i in range(k)]

if __name__ == "__main__":
    l = list(map(int, input().split()))
    k = int(input())

    print(heapk(l, k))
