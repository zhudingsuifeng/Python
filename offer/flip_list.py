#!/usr/bin/env python3
#coding = utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def insert(self, head):
        self.next = head
        return self

class Solution:
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            temp = pHead
            pHead = pHead.next
            temp.next = last
            last = temp
        return last

    def Reverse_List(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        l = []
        while pHead:
            tp = pHead
            pHead = pHead.next
            tp.next = None
            l.append(tp)
        head = l[0]
        for i in range(1, len(l)):
            l[i].next = head
            head = l[i]
        return head

if __name__ == "__main__":
    n = int(input())
    head = ListNode(None)
    for i in range(n, 0, -1):
        node = ListNode(i)
        head = node.insert(head)
    s = Solution()
    head = s.ReverseList(head)
    head = head.next
    while head:
        print(head.val)
        head = head.next
