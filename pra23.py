#!/usr/bin/python
# coding:utf-8
'''
star=['*']
for i in range(7):
    print star*(2*i+1)
'''
# 一定要注意python语言的对齐方式
from sys import stdout
for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print ' '
for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print ' '
