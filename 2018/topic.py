#!/usr/bin/env python3
#coding = utf-8

n = int(input())
t = []
for i in range(n):
    name, a, b = input().split()
    h = int(b)/int(a)
    if h <= 0.3:
        t.append(name + " " + str(5))
    elif h > 0.3 and h <= 0.6:
        t.append(name + " " + str(4))
    else:
        t.append(name + " " + str(3))
for j in sorted(t): 
    print(j)
    # sorted() 默认使用可迭代元素的第一个值排序
    # 也可以使用sorted(key = lambda x : x[2])来
