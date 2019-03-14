#!/usr/bin/env python3
#coding = utf-8

def brick(s):
    s = set(s)
    l = len(s)
    if l > 2:
        return 0
    elif l == 2:
        return 2
    elif l == 1:
        return 1

if __name__ == "__main__":
    s = input()
    print(brick(s))
