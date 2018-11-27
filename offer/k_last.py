#!/usr/bin/env python3
#coding = utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def insert(self, head):
        self.next = head
        head = self
        return head

class Solution:
    def FindKthToTail(self, head, k):
        l = []
        while head:
            l.append(head)
            head = head.next
        if k > len(l) or k < 1:
            return
        return l[-k]
        

if __name__ == "__main__":
    k = int(input())
    head = ListNode(16)
    for i in range(15, -1, -1):
        node = ListNode(i)
        head = node.insert(head)

    s = Solution()
    print(s.FindKthToTail(head, k).val)
