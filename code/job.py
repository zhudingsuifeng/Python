#!/usr/bin/env python3
#coding = utf-8

if __name__ == "__main__":
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    t=[l[0]]
    res=0
    while len(l)>1:
        if l[1]-l[0] <= 10:      # crossing
            t.append(l[1])
            l.pop(0)
        elif len(t)%3 == 0:
            t.append(l[1])
            l.pop(0)
        else:
            t.append(l[0]+10)    #insert a topic
            l[0] += 10
            res += 1
    if len(t)%3 == 0:
        print(res)
    else:
        print(res+3-len(t)%3) #the total can't be divisible by 3
