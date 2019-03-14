#!/usr/bin/env python3
#coding = utf-8

def indepent(x, f, d, p):
    if d/x <= f:
        return d//x
    else:
        return f+(d-x*f)//(p+x)

if __name__ == "__main__":
    x, f, d, p = map(int, input().split())
    print(indepent(x, f, d, p))
