#!/usr/bin/env python3
#coding = utf-8

# dynamic programming method
def dprogram(l, aim):
    if len(l) == 0 or aim < 0:
        return 0
    dp = [[ 0 for i in range(aim+1)] for i in range(len(l)) ]
    for i in range(len(l)):
        for j in range(aim+1):
            if i == 0:
                dp[0][j] =1 if j%l[0] == 0 else 0
            else:
                dp[i][j] = sum([ dp[i-1][k] for k in range(j, -1, -l[i])]) 
    return dp[-1][-1]

# optimized dynamic programming method 
def optdp(l, aim):
    if len(l) == 0 or aim < 0:
        return 0
    dp = [ [ 0 for j in range(aim+1)] for i in range(len(l))]
    #for i in range(aim+1):
        #dp[0][i] = 1 if i%l[0] == 0 else 0
    for i in range(0,len(l)):
        for j in range(aim+1):
            if i == 0:
                dp[i][j] = 1 if j%l[i] == 0 else 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-l[i]] if j-l[i] >= 0 else dp[i-1][j]
    print(dp)
    return dp[-1][-1]

# final optimized dynamic programming method 
def finaloptdp(l, aim):
    if len(l) == 0 or aim < 0:
        return 0
    dp = [1 if i%l[0] == 0 else 0  for i in range(aim+1)]
    for i in range(1, len(l)):
        for j in range(1, aim+1):
            dp[j] += dp[j-l[i]] if j-l[i] >= 0 else 0
    return dp[-1]

# recursive method
def coins(l, aim):
    if len(l) == 0 or aim < 0:
        return 0
    else:
        #return compose(l, 0, aim)
        return msearch(l, 0, aim)

def compose(l, index, aim):
    if index == len(l):
        res = 1 if aim == 0 else 0
    else:
        res = 0
        for i in range(0, aim//l[index]+1):
            res += compose(l, index+1, aim-l[index]*i)
    return res   # return a value each time when call coins(l,index,aim)

# memory search method
def msearch(l, index, aim):
    if index == len(l):
        res = 1 if aim == 0 else 0
    elif (index,aim) in mem:
        return mem[(index,aim)]
    else:
        res = 0
        for i in range(aim//l[index]+1):
            res += msearch(l, index+1, aim-l[index]*i)
    mem[(index,aim)] = res
    return res

def dfs(l, index, aim):
    if aim == 0:
        return 1
    elif (index, aim) in mem:
        return mem[(index, aim)]
    elif index > 0:
        if l[index] > aim:
            res = dfs(l, index -1, aim)
        else:
            res = dfs(l, index -1, aim) +dfs(l, index, aim-l[index])
    else:
        res = 1 if aim%l[index] == 0 else 0
    mem[(index, aim)] = res 
    return res

if __name__ == "__main__":
    aim = int(input())
    l = [1, 5, 10, 20, 50, 100]
    mem = {}

    #print(optdp(l, aim))
    print(dfs(l, len(l)-1, aim))
    #print(finaloptdp(l, aim))
    #print(coins(l, aim))
