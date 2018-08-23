#coding=utf-8
import copy
#python中的对象之间赋值时是按引用传递的，如果需要拷贝对象，需要使用标准库中的copy模块
#copy.copy浅拷贝，只拷贝父对象，不会拷贝对象的内部的子对象，就是说对原始对象中的子对象进行修改，copy对象不会改变
#copy.deepcopy深拷贝，拷贝对象及其子对象
a=[1,2,3,4,['a','b']]#原始对象
b=a #赋值，传递对象引用
c=copy.copy(a)#对象拷贝，浅拷贝
d=copy.deepcopy(a)#对象拷贝，深拷贝

a.append(10) #修改对象a
a[4].append('c') #修改对象a中的['a','b']数组对象

print('a=',a)
#print('b=',b) 
#print('c=',c) 
#print('d=',d) 
#list中添加元素,append()在列表末尾添加元素，insert()使用索引在列表任意位置添加元素，insert(索引,值)
#list中删除元素，del通过索引，可删除任意位置的元素
#使用pop()根据索引删除任意位置的元素，并返回删除的值，pop()默认删除最后一个元素
#使用remove()根据元素的值，来删除元素
for s in copy.copy(a):
	#对list有循环操作时，要使用copy，因为直接在原list上进行操作，会破坏循环,不能实现想要的效果
	print(s)
	a.pop()
print(a)