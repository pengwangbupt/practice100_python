#!/usr/bin/python
# coding:utf-8

def fun(n):
    if n==1:
        return 1
    else:
        return n*fun(n-1)

num = int(raw_input("Please input the number factorial:"))
print fun(num)
