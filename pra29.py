#!/usr/bin/python
# coding:utf-8

num = int(input("Please input the number(<=100000):"))
wang = num/10000
qian = num%10000/1000
bai = num%1000/100
shi =num%100/10
ge =num%10

if wang != 0:
    print "5 位数：",ge,shi,bai,qian,wang
elif qian != 0:
    print "4 位数：",ge,shi,bai,qian
elif bai != 0:
    print "3 位数：",ge,shi,bai
elif shi != 0:
    print "2 位数：",ge,shi
else:
    print "1 位数：",ge,shi,bai,qian,wang

