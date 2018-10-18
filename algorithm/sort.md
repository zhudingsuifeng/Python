## summary of sorting algorithms
### 冒泡排序(bubble sort)
- 冒泡排序是一种简单的排序算法。
```javascript
#!/usr/bin/env python3
#coding = utf-8
def bubble_sort(l):
 
```
### 选择排序(select sort)
```javascript
def select_sort(l):
    for i in range(len(l)-1):
        mindex = i
        for j in range(i+1, len(l)):
            if l[mindex] > l[j]:
                mindex = j
    return l
```
### 插入排序(insert sort)
```javascprit
```
### 希尔排序(shell sort)
### 归并排序(merge sort)
### 快速排序(quick sort)
### 堆排序(heap sort)
### 计数排序(counting sort)
### 桶排序(bucket sort)
### 基数排序(radix sort)
## 排序算法相关性质
### 稳定性
- 如果在待排序序列中，有多个相同的元素，经过排序之后，这些相同元素的相对位置没有发生改变，则称这个排序算法是稳定的，否则是不稳定的。
### 时间复杂度
- 时间复杂度的计算并不是计算程序具体运行的时间，而是算法执行语句的次数。
### 空间复杂度
- 空间复杂度是对一个算法在运行过程中临时占用存储空间大小的度量。

