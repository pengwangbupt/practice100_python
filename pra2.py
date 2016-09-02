#!/usr/bin/python
# -*- coding: utf-8 -*-

profit = int(raw_input("Please input the profit in this month:"))
reward = 0
if (profit > 1000000):
    reward += 0.01*(profit-1000000)+400000*0.015+200000*0.03+200000*0.05+100000*0.075+100000*0.1;
elif(profit > 600000)and(profit <= 1000000):
    reward += 0.15*(profit-600000)+200000*0.03+200000*0.05+100000*0.075+100000*0.1;
elif(profit > 400000)and(profit <= 600000):
    reward += 0.03*(profit-400000)+200000*0.05+100000*0.075+100000*0.1;
elif(profit > 200000)and(profit <= 400000):
    reward += 0.05*(profit-200000)+100000*0.075+100000*0.1;
elif(profit > 100000)and(profit <= 200000):
    reward += 0.075*(profit-100000)+100000*0.1;
else:
    reward += profit*0.1

print "The reward in this month is:",reward
