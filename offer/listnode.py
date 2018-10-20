#!/usr/bin/env python3
#coding = utf-8

class listNode:
    def __init__(self , x = None, p = None):
        self.val = x
        self.next = p

class Solution:
    def printListFromTailToHead(self, listNode):
        l = []
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]

if __name__ == "__main__":
    n = list(map(int, input().split()))
    p = None
    for i in n[::-1]:
        q = listNode()
        q.val = i
        q.next = p
        p = q

    # 类的使用，链表的简单实现
    s = Solution()
    print(s.printListFromTailToHead(p))
