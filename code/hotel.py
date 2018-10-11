#!/usr/bin/env python3
#coding = utf-8

if __name__ == "__main__":
    l = [0]*12

    while True:
        try:
            s = list(map(int, input().split()))
            l[s[0]:s[1]+1] = [s[2]]*(s[1]-s[0]+1)
        except:
            break

    p = []
    start, end, pp = 0, 0, 0
    while end < len(l):
        if l[end] != 0: 
            pp = l[end]
            start = end
            while l[end] == pp:
                end += 1
            p.append([start, end-1, pp])
        else:
            end += 1
    print(l)
    print(','.join(list(map(str, p))))
