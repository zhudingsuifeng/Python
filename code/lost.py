#!/usr/bin/env python
#coding=utf-8
#python3.6.5

print(int(''.join(sorted(set(map(str,range(1,10001)))-set(input().split()))))%7)
