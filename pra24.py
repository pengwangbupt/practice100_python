#!/usr/bin/python
# coding : utf-8

sum = 0
num1=1.0
num2=2.0
for i in range(20):
    num = num2/num1
    sum += num
    num = num2
    num2 = num1+num2
    num1 = num
print sum

