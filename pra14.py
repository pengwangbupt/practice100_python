#!/usr/bin/python
# coding:utf-8
"""
import math
prime=1;
num = int(raw_input("Please input a positive integer:"))
for i in range(2,int(math.sqrt(num)+1)):
    if(num%i==0):
        prime=0;
        break
if prime == 1:
    print "%d is a prime number"%num
else:
    for i in range(2,int(num/2)+1):
        if num%i==0:
            print i
            num = num/i
        else:
            break
"""
# 答案
from sys import stdout
n = int(raw_input("input number:\n"))
print "n = %d"%n

for i in range(2,n+1):
    while n!=1:
        if n%i == 0:
            stdout.write(str(i))
           # stdout.write("*")
            n = n/i
            if n == 1:
                pass
            else:
                stdout.write("*")
        else:
            break
# print "%d" % n
print " "
