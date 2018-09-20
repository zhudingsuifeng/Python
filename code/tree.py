#!/usr/bin/env python3
#coding = utf-8

#construct a tree and store the number of layers and the number of children in the node.
n = int(input())
tree={'0':[1,0]}  #tree{node:[1,0]} node in first layer and has 0 child.
for i in range(n-1):
    parent,children = input().split()
    if parent in tree and tree[parent][1]<2:
        tree[children] = [tree[parent][0]+1,0]
        tree[parent][1] += 1
depth = [x[0] for x in tree.values()]
#print(tree)
print(max(depth))
