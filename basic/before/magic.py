#coding=utf-8
#pop()直接删除末尾的元素，pop(1)删除指定元素
#insert(,)在指定位置添加元素，第一个参数是索引的位置，第二个是元素值
#append()函数，在list末尾添加新的元素
#extend()函数，合并两个list
"""
这实质上是参数的传递，并不是在原来的list中修改
def show_magicians(names):
	for name in names:
		print(name)
def make_great(names):
	Greatmagiciansnames=['The Great '+str(item) for item in names]
	return Greatmagiciansnames
magiciansnames=['hannah','ty','margot','huang']
show_magicians(magiciansnames)
Greatnames=make_great(magiciansnames)
show_magicians(Greatnames)
"""

def show_magicians(names):
	for name in names:
		print(name)
"""
#并没有找到很好的一个方法，临时建立一个list，承接修改好的list,把原来的list清空pop(),在原来list中append()临时list元素
#这个方法存在一个问题，就是需要一个临时数组，但是如果数据量非常大的话，可能造成内存空间不够，就是说空间代价较大
def make_great(names):
	greatnames=['The Great '+str(item) for item in names]
	while names:
		names.pop()
	for name in greatnames:
		names.append(name)
"""
#这是我设计的最终算法，只需要一个变量存储list长度，大大减少了空间复杂度
def make_great(names):
	i=0
	maximum=len(names)
	while i<maximum:
		names[i]='The Great '+names[i]
		i+=1
magiciansnames=['hannah','ty','margot','huang']
make_great(magiciansnames)
show_magicians(magiciansnames)