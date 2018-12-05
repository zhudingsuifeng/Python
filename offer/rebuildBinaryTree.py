#!/usr/bin/env python3
#coding = utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def levelTraversal(self, nodeList):
        if len(nodeList) == 0:
            return None
        if len(nodeList) == 1:
            return TreeNode(nodeList[0])
        Nodes = list(map(TreeNode, nodeList))
        root = Nodes[0]
        for i in range(len(Nodes)):
            node = Nodes[i]
            if i*2+1 < len(Nodes):
                node.left = Nodes[i*2+1]
            else:
                node.left = None
            if i*2+2 < len(Nodes):
                node.right = Nodes[i*2+2]
            else:
                node.right = None
        return root

    def preOrderTraversal(self, root):
        if not root:
            return []
        return [root.val] + self.preOrderTraversal(root.left) + self.preOrderTraversal(root.right)

    def inOrderTraversal(self, root):
        if not root:
            return []
        return self.inOrderTraversal(root.left) + [root.val] + self.inOrderTraversal(root.right)

    def postOrderTraversal(self, root):
        if not root:
            return []
        return self.postOrderTraversal(root.left) + self.postOrderTraversal(root.right) + [root.val]
        
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1], tin[:tin.index(pre[0])])
        root.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])
        return root

if __name__ == "__main__":
    nodeList = list(input().split())
    b = BinaryTree()
    root = b.levelTraversal(nodeList)
    root = b.reConstructBinaryTree(b.preOrderTraversal(root), b.inOrderTraversal(root))
    print(b.postOrderTraversal(root))
