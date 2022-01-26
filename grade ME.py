# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 21:17:34 2022

@author: acer
"""
M=input("數學成績?")
M=int(M)
E=input("英文成績?")
E=int(E)
if (M>=90 and E>=90):
    print("拿到獎學金")
elif (M==100 or E==100):
    print("拿到獎學金")
else:
    print("沒拿到獎學金")