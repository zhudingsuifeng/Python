#!/usr/bin/env python3
#coding = utf-8

def seq(n, l):
    return " ".join(l[n-1::-2] + l[n%2::2])  # 注意后半段开始位置与长度是奇数还是偶数有关

if __name__ == "__main__":
    n = int(input())
    l = input().split()
    print(seq(n, l))
