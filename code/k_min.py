#!/usr/bin/env python
#coding=utf-8
#python3.6.5

l=list(map(int,input().split()))
m=[str(i) for i in sorted(l[:len(l)-1])]  #list slice
print(' '.join(m[:l[-1]]))
