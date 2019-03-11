#!/usr/bin/env python3
#coding = utf-8

import dis

def swap1(a, b):
    temp = a
    a = b
    b = temp
    # return a, b

def swap2(a, b):
    a, b = b, a
    # return a, b

if __name__ == "__main__":
    print('--------------------------swap1-------------------------')
    print(dis.dis(swap1))
    print('--------------------------swap2-------------------------')
    print(dis.dis(swap2))

