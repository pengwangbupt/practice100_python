#!/usr/bin/python
# coding:utf-8

sum = 0
h = 100
for n in range(1,11):
    sum += h
    h = h/2.0
    print "n=%d,h=%f,sum=%f" %(n,h,sum)

