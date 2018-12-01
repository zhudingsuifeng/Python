#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if self.stack2 == []:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__ == "__main__":
    s = Solution()
    n = int(input())
    for i in range(n):
        s.push(i)
    print(s.pop())
    print(s.pop())
