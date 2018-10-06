#!/usr/bin/env python3
#coding=utf-8


# recursive method
def plan(l, aim):
    if len(l) == 0 or aim < 0:
        return 0
    else:
        # return subplan(l, 0, aim)
        return msearch(l, 0, aim)

def subplan(l, index, aim):
    if len(l) == index:
        res = 1 if aim == 0 else 0
    else:
        if aim < l[index]:
            res = subplan(l, index+1, aim)
        else:
            res = subplan(l, index+1, aim) + subplan(l, index+1, aim-l[index])
    return res

# memory search method
def msearch(l, index, aim):
    if len(l) == index:
        res = 1 if aim == 0 else 0
    elif (index, aim) in mem:
        res = mem[(index, aim)]
    else:
        if aim < l[index]:
            res = msearch(l, index+1, aim)
        else:
            res = msearch(l, index+1, aim) + msearch(l, index+1, aim-l[index])
    mem[(index, aim)] = res
    return res

# dynamic programming
def dprogram(l, aim):
    if len(l) == 0 or aim < 0:
        return 0
    dp = [ [ 0 for j in range(aim+1) ] for i in range(len(l))]
    for i in range(len(l)):
        for j in range(aim+1):
            if i == 0:
                dp[i][j] = 1 if j == 0 or j == l[i] else 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-l[i]] if j >= l[i] else dp[i-1][j]
    return dp[-1][-1]

# optimized dynamic programming
def optdp(l, aim):
    if len(l) == 0 or aim < 0:
        return 0
    dp = [ 1 if i == 0 or i == l[0] else 0 for i in range(aim+1)]
    for i in range(1, len(l)):
        for j in range(aim, 0, -1):
            dp[j] += dp[j-l[i]] if j-l[i] >=0 else 0
    return dp[-1]

if __name__ == "__main__":
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    mem = {}

    # print(optdp(A, m))
    print(plan(A, m))
