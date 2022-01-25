# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:52:40 2022

@author: acer
"""

G=input("成績?")
Gn=int(G)
if Gn>=0 and Gn<60:
    print("E")
if Gn>=60 and Gn<70:
    print("D")
if Gn>=70 and Gn<80:
    print("C")
if Gn>=80 and Gn<90:
    print("B")
if Gn>=90 and Gn<=100:
    print("A")