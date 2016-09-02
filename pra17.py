#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
统计字符串中的英文字母，空格，数字的个数

注意：中文字符=3个英文字符
"""
import string
s = raw_input('input a string:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
print 'char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others)
