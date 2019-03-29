#!/usr/bin/env python3
#coding = utf-8

def times(s, num):
    return s*int(num)

if __name__ == "__main__":
    s, num = input().split()
    print(times(s, num))
