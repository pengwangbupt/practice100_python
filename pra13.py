#!/usr/bin/python
# coding:utf-8

import math
for i in range(100,1000):
    bai=i/100
    shi=i%100/10
    ge=i%10
    if(bai*bai*bai+shi*shi*shi+ge*ge*ge==i):
        print i

