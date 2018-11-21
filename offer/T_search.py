#!/usr/bin/env python3
#coding = utf-8

class Solution:
    # array two-dimensional list
    def Find(self, target, array):
        n = len(array) - 1 
        m = 0
        while n > -1 and m < len(array[0]):
            print(array[n][m])
            if array[n][m] == target:
                return True
            elif array[n][m] < target:
                m += 1
            else:
                n -= 1
        return False


if __name__ == "__main__":
    k = int(input())
    l = []
    while True:
        t = list(map(int, input().split()))
        if t:
            l.append(t)
        else:
            break
    f = Solution()
    print(f.Find(k, l))
