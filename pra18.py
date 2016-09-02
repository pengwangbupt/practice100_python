#!/usr/bin/python
# coding:utf-8

num=int(raw_input("Please input a number between 0~9:"))
n=int(raw_input("Please input the number of calculate:"))

sum = num

for i in range(2,n+1):
    sum+=num*10+num
    num=num*10+num

print sum
