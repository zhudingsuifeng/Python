#!/usr/bin/env python3
#coding = utf-8

# a^b = c then a^c = b 
def mixing(n, l):
    res = 0
    while len(l) > 2:
        l = sorted(l, reverse = True)  # number with more digits are prioritized
        t = l[0]^l[1]
        if t < l[1]:   # make sure the highest digits are the same
            if t not in l:
                l.append(t)
        else:
            res += 1
        l.pop(0)
    return res + len(l)

if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))

    print(mixing(n, l))
