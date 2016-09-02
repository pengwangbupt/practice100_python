#!/usr/bin/python
# coding:utf-8

score = int(raw_input("Please input the score:"))
if score >= 90:
    print 'A'
elif 60 <= score < 89:
    print 'B'
else:
    print 'C'
