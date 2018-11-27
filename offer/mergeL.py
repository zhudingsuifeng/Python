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
    def Merge(self, pHead1, pHead2):
        head = p = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                p.next = pHead1
                p = p.next
                pHead1 = pHead1.next
            else:
                p.next = pHead2
                p = p.next
                pHead2 = pHead2.next
        if pHead1:
            p.next = pHead1
        else:
            p.next = pHead2
        return head.next

if __name__ == "__main__":
    pHead1 = ListNode(18)
    for i in range(16, 1, -2):
        node = ListNode(i)
        pHead1 = node.insert(pHead1)

    pHead2 = ListNode(17)
    for i in range(15, 1, -2):
        node = ListNode(i)
        pHead2 = node.insert(pHead2)

    s = Solution()
    l = s.Merge(pHead1, pHead2)
    while l:
        print(l.val)
        l = l.next
