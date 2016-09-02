#!/usr/bin/python
# coding:utf-8

def age(n):
    if n == 1:
        return 10
    else:
        return 2+age(n-1)

print age(5)
