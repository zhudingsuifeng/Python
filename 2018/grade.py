#!/usr/bin/env python3
#coding = utf-8

def grade(n, l):
    l = sorted(l)
    t = l[0] - l[1]
    for i in range(1, n):
        if l[i-1] - l[i] != t:
            return 'Impossible'
    else:
        return 'Possible'

if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    print(grade(n, l))
