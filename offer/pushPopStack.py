#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) != len(popV):
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if popV:
            return False
        return True

if __name__ == "__main__":
    pushV = list(input().split())
    popV = list(input().split())
    s = Solution()
    print(s.IsPopOrder(pushV, popV))
