#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
(1)斐波那契数列

"""
fse=0
fse1=0
fse2=1
for i in range(100):
    print fse
    fse = fse1+fse2
    fse2=fse1
    fse1=fse
"""
(2)斐波那契数列一般是用 “递归” 实现的

"""

def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

# 输出第N个斐波那契数列
N=int(raw_input("请输入N："))
print fib(N)

"""
(3)递归实现
"""
def fib1(n):
    if n==1 or n==2:
        return 1
    return fib1(n-1)+fib1(n-2)
# 输出第N个斐波那契数列
N=int(raw_input("请输入N："))
print fib1(N)
