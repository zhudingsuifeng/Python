#!/usr/bin/env python3
#coding = utf-8

# 本地调试没有问题，在线显示越界
def bracket(b):
    res = [b[0]]
    for i in range(1,len(b)):
        if res and b[i] == ')' and res[-1] == '(':
            res.pop()
        else:
            res.append(b[i])
    return len(res)

def brack(b):
    while "()" in b:
        b = b.replace("()", "")
    return len(b)

if __name__ == "__main__":
    b = input()
    print(brack(b))
