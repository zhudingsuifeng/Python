#!/usr/bin/env python
#coding=utf-8
filename='pi.txt'
with open(filename) as file_object:
#    for line in file_object:   line并不是关键字，对文件对象使用for in默认时一行一行的 
    for s in file_object:
	print(s)
