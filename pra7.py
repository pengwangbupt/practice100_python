#!/usr/bin/python
# coding:utf-8

"""
7 将一个列表的数据复制到另一个列表中
"""

#（1）
list1=[1,2,3,4]
list2=[]
list1_num=len(list1)
for i in range(list1_num-1):
    list2.append( list1[i] )
print list2

# (2)
a = [1,2,3]
b = a[:]
print b,id(a),id(b) 
