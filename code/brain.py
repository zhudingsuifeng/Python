#!/usr/bin/env python3
#coding = utf-8

import re

def brain(s, a, b):
    m = re.compile(r'.*%s.*%s.*' % (a, b))
    # compile a regular expression and generate a regular expression object.
    t = s[::-1]
    res = re.search(m, s)
    # scans the entire string and returns the first successful match.
    temp = re.search(m, t)
    if res and temp:
        print("both")
    elif res:
        print("forward")
    elif temp:
        print("backward")
    else:
        print("invalid")

if __name__ == "__main__":
    s = input()
    a = input()
    b = input()
    brain(s, a, b)
    
