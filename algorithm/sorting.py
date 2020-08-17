#!/usr/bin/env python3
#coding = utf-8

import random

# 原始冒泡排序
def basic_bubble(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

# 带标识的冒泡排序
def flag_bubble(l):
    for i in range(len(l)-1):
        flag = 0
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j+1], l[j] = l[j], l[j+1]
                flag = 1
        if flag == 0:  # 一轮比较下来，没有元素交换位置，已经有序，提前返回
            return l
    return l

# 截断式冒泡排序
def cut_bubble(l):
    bg = len(l)-1
    for _ in range(len(l)-1):
        flag = 0
        j = 0
        while j < bg:   # 边界
            if l[j] > l[j+1]:
                l[j+1], l[j] = l[j], l[j+1]
                flag = 1
                tbg = j   # 记录每一轮最后交换的位置
            j += 1
        bg = tbg   # 无序的内容进行比较，已经有序的不在比较
        if flag == 0:
            return l
    return l

# 原始鸡尾酒排序，双向冒泡排序
def origin_cocktail_bubble(l):
    if len(l) <= 1:
        return l
    else:
        for i in range(len(l)//2):  # 每一次大循环，确定最大和最小两个数字
            for j in range(i, len(l)-i-1):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
            for k in range(len(l)-i-1, 0, -1):
                if l[k] < l[k-1]:
                    l[k], l[k-1] = l[k-1], l[k]
        return l

# 带标识位，带边界的鸡尾酒排序
def optimize_cocktail_bubble(l):
    top, down = len(l)-1, 0  # 注意边界
    j, k = 0, len(l)-1
    for _ in range(len(l)//2):
        flag = 0
        while j < top:
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                flag = 1
                ttop = j
            j += 1
        top = ttop   # 找到有序无序上边界
        while k > down:
            if l[k] < l[k-1]:
                l[k], l[k-1] = l[k-1], l[k]
                flag = 1
                tdown = k
            k -= 1
        down = tdown  # 有序无序下边界
        j, k = down, top
        if flag == 0:   # 已经有序，提前返回
            return l
    return l

# select sort
def select_sort(l):
    for i in range(len(l)-1):
        mindex = i
        for j in range(i+1, len(l)):
            if l[mindex] > l[j]:
                mindex = j
        l[i], l[mindex] = l[mindex], l[i]
    return l

# insert sort
def insert_sort(l):
    for i in range(1, len(l)):
        preIndex = i-1
        temp = l[i]
        while preIndex >= 0 and l[preIndex] > temp: 
            l[preIndex+1] = l[preIndex]
            preIndex -= 1
        l[preIndex+1] = temp
    return l

# shell sort
def shell_sort(l):
    for gap in range(len(l)//3, 0, -1):
        print(gap)
        print(l)
        for i in range(gap):
            for j in range(i+gap, len(l), gap):
                preIndex = j-gap
                temp = l[j]
                while preIndex >= 0 and l[preIndex] > temp:
                    l[preIndex+gap] = l[preIndex]
                    preIndex -= gap
                l[preIndex+gap] = temp
    return l

if __name__ == "__main__":
    l = [i for i in range(10)]
    random.shuffle(l)
    print(l)

    print(optimize_cocktail_bubble(l))
    # print(0)