#!/usr/bin/python
# -*- coding: utf-8 -*-

x = int(input("please input x:"))
y = int(input("please input y:"))
z = int(input("please input z:"))

if (x>y):
    if(x>z):
        if(y>z):
            print "z=%d,y=%d,x=%d"%(z,y,x)
        else:
            print "y=%d,z=%d,x=%d"%(y,z,x)
    else:
        print "y=%d,x=%d,x=%d"%(y,x,z)
else:
    if(x>z):
        print "z=%d,x=%d,y=%d"%(z,x,y)
    else:
        if(y>z):
            print "x=%d,z=%d,y=%d"%(x,z,y)
        else:
            print "x=%d,y=%d,z=%d"%(x,y,z)
# 其实可以用更简单的方法：答案如下
l = [] # list
for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)
l.sort()
print l
