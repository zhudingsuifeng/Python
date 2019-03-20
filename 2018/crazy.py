#!/usr/bin/env python3
#coding = utf-8

def crazy(n: int, h: [int]) -> int:
    if len(h) == 1:
        return 0
    else:
        h = sorted(h)
        if n % 2 == 0:
            return 2*sum(h[n//2+1:]) + h[n//2] - 2*sum(h[:n//2-1]) - h[n//2-1]
        else:
            t1 = 2*sum(h[n//2+1:]) - 2*sum(h[:n//2-1]) - sum(h[n//2-1:n//2+1])
            t2 = 2*sum(h[n//2+2:]) + sum(h[n//2:n//2+2]) - 2*sum(h[:n//2])
            return max(t1, t2)

if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))
    print(crazy(n, h))
