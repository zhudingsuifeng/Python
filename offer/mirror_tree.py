#!/usr/bin/env python3
#coding = utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def get_root(self):
        return self.root

    def add(self, node):
        if self.root is None:
            self.root = node
        else:
            q =[self.root]
            while True:
                p = q.pop(0)
                if p.left == None:
                    p.left = node 
                    return 
                elif p.right == None:
                    p.right = node
                    return 
                else:
                    q.append(p.left)
                    q.append(p.right)

    def Mirror(self, root):
        if root != None:
            root.left, root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)

    def pList(self):
        if self.root == None:
            return
        q = [self.root]
        l = []
        while len(q) > 0:
            p = q.pop(0)
            l.append(p.val)
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)
        return l
            
if __name__ == "__main__":
    n = int(input())
    b = BinaryTree()
    for i in range(n):
        node = TreeNode(i)
        b.add(node)
    print(b.pList())
    root = b.get_root()
    b.Mirror(root)
    print('\n')
    print(b.pList())
