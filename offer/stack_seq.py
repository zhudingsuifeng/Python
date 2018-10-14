#!/usr/bin/env python3
#coding = utf-8

def IsPopOrder(inseq, outseq):
    if len(inseq) != len(outseq):
        return "No"
    stack = []
    for i in inseq:
        stack.append(i)
        while len(stack) and  stack[-1] == outseq[0]:
            stack.pop(-1)
            outseq.pop(0)
    if len(stack):
        return "No"
    return "Yes"

if __name__ == "__main__":
    inseq = input().split()
    outseq = input().split()

    print(IsPopOrder(inseq, outseq))
