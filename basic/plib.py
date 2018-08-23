#!/usr/bin/env python
#coding=utf-8
"""
Create on Tue May 15 10:12:49 2018
@author:fly
python tutorial.
"""
import re
import os
import sys
import numpy as np
import math
import string
import pickle
from math import pi as PI

#calculate the area of the circle
def CircleArea(r):
	try:
		r=int(r)
		return PI*r*r
	except:
		print('You must give me an integer or float as radius.')

#
def demo(para):
	try:
		para=para.split()
		para=map(float,para)
		avg=sum(para)/len(para)
		g=[i for i in para if i>avg]
		return (avg,)+tuple(g)
	except:
		print('You must give me an integer or float array as input')

#
def Ss(s):
	result=[0,0]
	for ch in s:
		if 'a'<=ch<='z':
			result[1]+=1
		elif 'A'<=ch<='Z':
			result[0]+=1
	return result

#
def sorting(l,k):
	l=l.split()
	l=map(int,l)
	k=int(k)
	if len(l)<k:
		print("please input data correctly")
	else:
		nl=l[k-1::-1]+[l[k]]+l[:k:-1]
		nl=nl[::-1]
		return nl

#
def small(lst):
	lst=map(int,lst.split())
	s=min(lst)
	i=[index for index,value in enumerate(lst) if value==s]
	return (s,)+tuple(i)

#
def acc(o,i):
	if not(isinstance(o,str) and isinstance(i,str)):
		print('The two parameters must be strings')
		return
	if len(o)!=len(i):
		print("Sorry.I suppose the second parameter string is shorter.")
		return
	l=0
	for o_c,i_c in zip(o,i):
		if o_c==i_c:
			l+=1
	return float(l)/len(o)

#array class
class MyArray(object):
	def __IsNumber(self,n):
		if not isinstance(n,(int,float)):
			return False
		return True
	def __init__(self,*args):
		if not args:
			self.__value=[]
		else:
			for arg in args:
				if not self.__IsNumber(arg):
					print("All elements must be number")
					return
			self.__value=list(args)
	def __del__(self):
		del self.__value
	def __add__(self,n):
		if self.__IsNumber(n):
			b=MyArray()
			b.__value=[item+n for item in self.__value]
			return b
		elif isinstance (n,MyArray):
			if len(n.__value)==len(self.__value):
				c=MyArray()
				c.__value=[i+j for i,j in zip(self.__value,n.__value)]
				return c
			else:
				print("Lenght not equal")
		else:
			print("Not supported")
	def __sub__(self,n):
		if not self.__IsNumber(n):
			print("- operating with ",type(n)," and number type is not supported.")
			return
		b=MyArray()
		b.__value=[item-n for item in self.__value]
		return b
	def __mod__(self,n):
		if not self.__IsNumber(n):
			print("% operating with ",type(n)," and number type is not supported.")
			return
		b=MyArray()
		b.__value=[item%n for item in self.__value]
		return b
	def append(self,v):
		if not self.__IsNumber(v):
			print("Only number can be appended.")
			return
		self.__value.append(v)
	def __getitem__(self,index):
		l=len(self.__value)
		if isinstance(index,int) and 0<=index<l:
			return self.__value[index]
		elif isinstance(index,(list,tuple)):
			result=[]
			for i in index:
				if not(isinstance(i,int)and 0<=i<l):
					return 'index error'
				result.append(self.__value[i])
			return result
		else:
			return 'index error'				
	def __setitem__(self,index,value):
		l=len(self.__value)
		if isinstance(index,int) and 0<=index<=l:
			self.__value[index]=value
		elif isinstance(index,(list,tuple)):
			for i in index:
				if not(isinstance(i,int)and 0<=i<=l):
					raise Exception('index error')
			if isinstance(value,(list,tuple)):
				if len(index)==len(value):
					for i,v in enumerate(index):
						self.__value[v]=value[i]
				else:
					raise Exception('values and index must be of the same length')
			elif isinstance(value,(int,float,complex)):
				for i in index:
					self.__value[i]=value
			else:
				raise Exception('value error')
		else:
			raise Exception('index error')

	def __contains(self,v):
		if v in self.__value:
			return True
		return False
	def __eq__(self,v):
		if not isinstance(v,MyArray):
			print(v,' must be an instance of MyArray.')
			return False
		if self.__value==v.__valuse:
			return True
		return False
	def show(self):
		print(self.__value)

#
class Set(object):
	def __init__(self,data=None):
		if data==None:
			self.__data=[]
		else:
			if not hasattr(data,'__iter__'):
				raise Exception('must iterate')
			temp=[]
			for item in data:
				hash(item)
				if not item in temp:
					temp.append(item)
			self.__data=temp
	def __del__(self):
		del self.__data
	def add(self,value):
		hash(value)
		if value not in self.__data:
			self.__data.append(value)
		else:
			print('element already exist')
	def remove(self,value):
		if value in self.__data:
			self.__data.remove(value)
			print('remove sucess')
		else:
			print('element not exist')
	def __sub__(self,oset):
		if not isinstance(oset,Set):
			print('type error')
		result=Set()
		for item in self.__data:
			if item not in oset.__data:
				result.__data.append(item)
		return result
	def __and__(self,oset):
		if not isinstance(oset,Set):
			print('type error')
		result=Set()
		for item in self.__data:
			if item in oset.__data:
				result.__data.append(item)
		return result
	def __or__(self,oset):
		if not isinstance(oset,Set):
			print('type error')
		result=Set(self.__data)
		for item in oset.__data:
			if item not in result.__data:
				result.__data.append(item)
		return result
	def __eq__(self,oset):
		if not isinstance(oset,Set):
			print('type error')
		if sorted(self.__data)==sorted(oset.__data):
			return True
		else:
			return False
	def show(self):
		print(self.__data)

#
def _identifyClassNames(index,line):
	pass
def _identifyFunctionNames(index,line):
	pass
def _identifyVariableNames(index,line):
	pass
def output():
	pass

if __name__=="__main__":
	#s=raw_input("origin string:")
	#n=raw_input("another string:")
	#print(CircleArea(s))
	#print(acc(s,n))
	#x=Set([1,2,3,4,5,6])
	#y=Set([7,3,8,9,5])
	#x.show()
	#(x-y).show()
	#(x|y).show()
	#(x&y).show()
	#intab="abcd"
	#outtab="1234"
	#table=string.maketrans(intab,outtab)
	#test="adfsdffsdabcdsdfsdfs"
	#print(test.translate(table))
	n=7
	i=13000000
	lst=[1,2,3]
	f=open('samp.dat','wb')
	try:
		pickle.dump(n,f)
		pickle.dump(i,f)
		pickle.dump(lst,f)
	except:
		print('write error')
	finally:
		f.close()
	nf=open('samp.dat','rb')
	print(pickle.load(nf))
	nf.close()
	print("success")
