# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 00:02:44 2024

@author: HP
"""

a=int(input("nhap nam: "))
b=int(input("nhap thang: "))
if a%4 ==0 and a%100!=0 or a %400==0:
    print ("do la nam nhuan")
    if b==2:
        print("thang do co 29 ngay")
else:
    print("do khong phai nam nhuan")
    if b==2:
        print("thang co 28 ngay")
if b in [1,3,5,7,8,10,12]:
    print("thang co 31 ngay")
if b in [4,6,9,11]:
    print("thang co 30 ngay")