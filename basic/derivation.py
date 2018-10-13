#!/usr/bin/env python3
#coding = utf-8

# list derivation
n = [ 3, 5, 6 ,4, 20, 10, 1, 2, 6, 3, 4]
s = sum([ i for i in n if i > 6])
print(s)

# dictionary derivation
a = {'a':10,'b':20,'A':3,'B':6}
f = { x: a.get(x.lower()) + a.get(x.upper()) for x in a.keys() if x.islower()}
b = { i.lower() : a.get(i.lower()) + a.get(i.upper()) for i in a.keys() if i in ['a']}

# print(f)
# print(b)
