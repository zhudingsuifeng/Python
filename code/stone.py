#!/usr/bin/env python3
#coding = utf-8

def jump(n, m):
    if n == m:
        return 0
    # get the approximation of the corresponding number
    app = [ [] for i in range(m+1)]
    for i in range(2, m+1):
        for j in range(i+i, m+1, i):
            app[j].append(i)

    # print(app)
    dp = [m]*(m+1)
    dp[n] = 0
    for i in range(n, m+1):
        if dp[i] < m:
            for j in app[i]:
                if i+j < m+1:
                    dp[i+j] = min(dp[i+j],dp[i]+1) 
    # print(dp)
    if dp[-1] < m:
        return dp[-1]
    else:
        return -1

if __name__ == "__main__":
    n, m = map(int, input().split())

    print(jump(n, m))
