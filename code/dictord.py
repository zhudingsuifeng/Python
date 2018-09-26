#!/usr/bin/env python3
#coding = utf-8

n,m = map(int,input().split())
i = 1
m -= 1

while m > 0:
    start = i
    end = start+1
    num = 0
    while start <= n:
        num += min(end,n+1)-start
        start *= 10
        end *= 10
    if num > m:
        i *= 10
        m -= 1
    else:
        i += 1         # num = 1 ... 2 elements 
        m -= num

print(i)

#res = i = 1
#
#while i < m:
#    #print(res,i)
#    if res*10 <= n: # 1 10 100 1000 ...
#        res *= 10
#    elif res+1 <= n and (res+1)%10 != 0: # 101 102 103 ... 109 
#        res += 1
#    else:
#        res = res//10+1  # 1 10 2
#        while res%10 == 0:
#            res = res//10
#    i += 1
#
#print(res)
#
#l=list(map(str,[ i for i in range(1,n+1) ]))
#print(sorted(l)[m-1])
