#!/usr/bin/env python
#coding=utf-8
import numpy
import random
import codecs
import copy
import re
import matplotlib.pyplot as plt

def calcuDistance(vec1,vec2):
	"""计算向量vec1和向量vec2之间的欧氏距离"""
	return numpy.sqrt(numpy.sum(numpy.square(vec1-vec2)))
	#sqrt()求平方根,sum()求数组所有元素的和,square()求平方,数学上来说，就是两个点之间的距离公式
def loadDataSet(inFile):
	"""载入数据测试数据集"""
	#数据由文本保存，为二维坐标
	inData=codecs.open(inFile,'r','utf-8').readlines()
	dataSet=list()#list()方法用于将元组转换为列表
	for line in inData:
		line=line.strip()#s.strip(rm)删除s字符串中开头、结尾处，位于rm删除序列的字符
		strList=re.split('[ ]+',line)#除去多余的空格，python的str类有split方法，但是这个split方法只能根据指定的某个字符分隔字符串，如果要同时指定多个字符来分割字符串，可以使用python的re模块中提供的split方法来做这件事请。
		#re.split(';|,',str)前一个参数是用来分割的字符，|分割开多个分个字符，str被分割的字符串。
		#print strList[0],strList[1]
		numList=list()
		for item in strList:
			num=float(item)
			numList.append(num)
			#print numList
		dataSet.append(numList)
	return dataSet 
def initCentroids(dataSet,k):
	"""初始化k个质心，随机获取"""
	return random.sample(dataSet,k)#从dataSet中随机获取k个数据项返回
def minDistance(dataSet,centroidList):
	"""对每个属于dataSet的item,计算item与centroidList中k个质心的欧氏距离，找出距离最小的，并将item加入相应的簇类中"""
	clusterDist=dict()#用dict来保存簇类结果，dict()生成一个空的字典{key:value}
	for item in dataSet:
		vec1=numpy.array(item)#转换成array形式
		flag=0         #簇分类标记，记录与相应簇距离最近的那个簇
		minDis=float("inf")   #初始化为最大值
		for i in range(len(centroidList)):
			vec2=numpy.array(centroidList[i])
			distance=calcuDistance(vec1,vec2)#计算相应的欧氏距离
			if distance<minDis:
				minDis=distance
				flag=i      #结束循环，flag保存的是与当前item距离最近的那个簇标记
		if flag not in clusterDist.keys():  #簇标记不存在，进行初始化
			clusterDist[flag]=list()
			#print flag,item
		clusterDist[flag].append(item)#加入相应的类别中
	return clusterDist     #返回新的聚类结果
def getCentroids(clusterDict):
	"""得到k个质心"""
	centroidList=list()
	for key in clusterDict.keys():
		centroid=numpy.mean(numpy.array(clusterDict[key]),axis=0)#计算每列的平均值，即找到质心
		#print key,centroid
		centroidList.append(centroid)
	return numpy.array(centroidList).tolist()#list中元素类型可以不通
def getVar(clusterDist,centroidList):
	"""计算簇集合间的均方误差，将簇类中各个向量与质心的距离进行累加求和"""
	sum=0.0
	for key in clusterDist.keys():#clusterDist类列表
		vec1=numpy.array(centroidList[key])#centroidList每个类中元素列表
		distance=0.0
		for item in clusterDist[key]:
			vec2=numpy.array(item)
			distance+=calcuDistance(vec1,vec2)
		sum+=distance
	return sum
def showCluster(centroidList,clusterDict):
	"""展示聚类结果"""
	colorMark=['or','ob','og','ok','oy','ow']  #不同簇类的标记'or'-->'o'代表圆，'r'代表red,'b':blue
	centroidMark=['dr','db','dg','dk','dy','dw']#质心标记，同上'd'代表菱形
	for key in clusterDict.keys():
		plt.plot(centroidList[key][0],centroidList[key][1],centroidMark[key],markersize=12)    #画质心点
		for item in clusterDict[key]:
			plt.plot(item[0],item[1],colorMark[key])    #画簇类下的点,plot(x,y,c)三个参数，x坐标，y坐标,c颜色，形状
	plt.show()
if __name__ == '__main__':
	inFile="testSet.txt"       #数据及文件
	dataSet=loadDataSet(inFile)#载入数据集
	centroidList=initCentroids(dataSet,6)#初始化质心，设置k=6
	clusterDict=minDistance(dataSet, centroidList) #第一次聚类迭代
	newVar=getVar(clusterDict, centroidList)#获得均方误差值，通过新旧
	oldVar=-0.0001     #旧均方误差值初始化为-1
	print '******第一次迭代******'
	print
	print '簇类'
	for key in clusterDict.keys():
		print key,'-->',clusterDict[key]
	print 'k个均值向量',centroidList
	print '平均均方误差：',newVar
	print
	showCluster(centroidList, clusterDict)#展示聚类结果
	k=2
	while abs(newVar-oldVar)>=0.0001:#当连续两次聚类结果小于0.0001时，迭代结束
		centroidList=getCentroids(clusterDict)#获得新的质心
		clusterDict=minDistance(dataSet, centroidList)#新的聚类结果
		oldVar=newVar
		newVar=getVar(clusterDict, centroidList)
		print '******第%d次迭代******' % k
		print
		print '簇类'
		for key in clusterDict.keys():
			print key,'-->',clusterDict[key]
		print 'k个均值向量',centroidList
		print '平均均方误差：',newVar
		print 
		showCluster(centroidList,clusterDict)#展示聚类结果
		k+=1