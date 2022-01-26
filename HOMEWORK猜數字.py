# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:40:13 2022

@author: acer
"""
import random
N=random.randint(1,10)

i=1
while i <=5:

    M=input("數字:")
    M=int(M)
    if i==5:
        print("你輸了")
    elif M==N:
        print("猜對了")
        break
    elif M>N:
        print("數字太大")
        i=i+1
    elif M<N:
        print("數字太小")
        i=i+1
    
   