#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        if not self.min_stack or self.min_stack[-1] >= node:
            self.min_stack.append(node)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]

    def getStack(self):
        return self.stack

if __name__ == "__main__":
    l = list(map(int, input().split()))
    s = Solution()
    for i in l:
        s.push(i)
        print(s.getStack())
        print(s.min())
    print("success")
