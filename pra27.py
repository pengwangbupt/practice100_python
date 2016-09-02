#!/usr/bin/python
# coding:utf-8

def output(s,n):
    if n == 0:
        return
    print (s[n-1])
    output(s,n-1)

# num = int(input("Please input the number of characters:"))
s = raw_input("Please input character:")
num = len(s)
print "The number of characters is %d" % num
output(s,num)
