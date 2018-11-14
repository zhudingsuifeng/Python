#!/usr/bin/env python3
#coding = utf-8

# basic bubble sort
def bubble_sort(l):
    for i in range(len(l), 0, -1):
        for j in range(i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

# change flag bubble sort
def flag_bubble(l):
    for i in range(len(l), 0, -1):
        flag = False
        for j in range(i-1):
            if l[j] > l[j+1]:
                flag = True
                l[j], l[j+1] = l[j+1], l[j]
        if flag == False: # end loop if there is no exchange in this round
            break
    return l

# double bubble (cocktail sorting)
def cocktail_bubble(l):
    low, high = 0, len(l)-1
    while low < high: # list is disordered when it's between low and high
        p = low
        for i in range(low, high): # low -> high ,watch out the boundary
            if l[i] > l[i+1]:
                l[i+1], l[i] = l[i], l[i+1]
                p = i
        high = p
        for j in range(high, low, -1): # high -> low
            if l[j] < l[j-1]:
                l[j-1], l[j] = l[j], l[j-1]
                p = j
        low = p
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
    l = list(map(int, input().split()))

    print(' '.join(list(map(str, shell_sort(l)))))
    # print(0)
