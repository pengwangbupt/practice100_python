#!/usr/bin/python
# -*- coding: utf-8 -*-

year = input("请输入某年：")
month = input("请输入某月：")
day = input("请输入某日：")

if(year%4==0 and year%100!=0)or(year%400==0):
    leap_year = 1;
else:
    leap_year = 0;
months=(0,31,59,90,120,151,181,212,243,273,304,334)
if 0<month<=12:
    sum = months[month-1]
    if (leap_year==1)and(month>2):
        sum+=1
else:
    print 'data error'
sum+=day
print 'it is the %dth day.' % sum

