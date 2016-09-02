#!/usr/bin/python
# coding:utf-8

from sys import stdout
s=[]
for i in range(2,1001):
    sum = 0
    flag=0
    for j in range(2,i):
        if (i%j == 0):
            sum+=j
           # stdout.write(str(j))
     #       sum+=(i/j)
            
    if (i==(sum+1)):
        print i
  #  if flag==1:
  #      print i
