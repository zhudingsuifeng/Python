#!/usr/bin/env python3
#coding = utf-8

def sum_odd(n):   #dynamic programming ,recursive conversion function
    l = [0]*(n + 1)
    for i in range(1, n+1):
        if i % 2 != 0:
            l[i] = i
        else:
            l[i] = l[i//2]
    print(l)
    print(sum(l))

# equal difference series summation
# 1 2 3 4 5 6 7 8 9 10
# 1 3 5 7 9  sum and n//2
# 1 2 3 4  sum 1 3 and n//2
def equal_sum(n):
    res = 0
    while n > 0:
        res += ((n + 1)//2)**2
        n //=2
    print(res)

if __name__ == "__main__":
    n = int(input())
    #sum_odd(n)
    equal_sum(n)
