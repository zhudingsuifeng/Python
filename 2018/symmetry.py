#!/usr/bin/env python3
#coding = utf-8

def isPrime(n):
    if n > 1:
        for i in range(2, n//2+1):
            if n%i == 0:
                return False
        else:
            return True


def judge(l, r):
    res = 0
    for num in range(l, r+1):
        if num > 1:
            for i in range(2, num//2+1):
                if num%i == 0:
                    break
            else:
                num = str(num)
                for j in range(len(num)//2):
                    if num[j] != num[len(num)-j-1]:
                        break
                else:
                    res += 1
    return res

if __name__ == "__main__":
    l, r = map(int, input().split())
    print(judge(l, r))
