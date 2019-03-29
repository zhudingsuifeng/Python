#!/usr/bin/env python3
#coding = utf-8

n, m = map(int, input().split())
men = 0
for i in range(n):
    men = max(men, int(input().split()[0]))
lady = 0
for j in range(m):
    lady = max(lady, int(input().split()[0]))
print(max(men, lady))
