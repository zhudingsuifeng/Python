## summary of sorting algorithms
### 冒泡排序(bubble sort)
- 冒泡排序是一种简单的排序算法。他重复的走访要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访序列的工作是重复进行直到没有再需要交换，也就是说该序列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢浮到数列的顶端。
- 算法描述
    + 比较相邻的元素。如果第一个比第二个大，就交换他们两个；
    + 对每一对相邻元素做同样的工作，开始第一对到结尾的最后一对，这样在最后的元素应该会使最大的数；
    + 针对所有的元素重复以上的步骤，除了最后一个；
    + 重复步骤1～3，直到排序完成。  
![bubble sort](images/bubble_sort.gif)
```javascript
#!/usr/bin/env python3
#coding = utf-8
def bubble_sort(l):
    for i in range(len(l), 0, -1):
        for j in range(i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
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

