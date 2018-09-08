#!/usr/bin/env python
#coding=utf-8
#python3.6.5

s=input()

if s.upper()!=s:
    print("Dislikes")
else:
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            print("Dislikes")
            break
    else:
        print("Likes")
