#!/usr/bin/python
# coding:utf-8

num = int(raw_input("Please input a number:"))

s=str(num)  # 很重要的哦！！str函数，将整数转化为字符串
x = len(s)
print x

flag = True

for i in range(x):
    if s[i] != s[x-i-1]:
        flag = False
if flag ==  True:
    print "%d 是回文数" % num
else:
    print "%d 不是回文数" % num
