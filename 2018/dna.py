#!/usr/bin/env python3
#coding = utf-8

import itertools

def dna(s):
    for i in range(1, len(s)+1):
        for j in itertools.product('ACGT', repeat = i):
            if ''.join(j) not in s:
                return i

if __name__ == "__main__":
    s = input()
    print(dna(s))
