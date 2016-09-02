#!/usr/bin/python
# coding:utf-8

import math

num=0

for i in range(101,200):
    flag=1
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j == 0:
            flag=0
            break
            
    if flag == 1:
        num += 1
        print i
print "the total is %d" % num
