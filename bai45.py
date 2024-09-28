# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:13:37 2024

@author: HP
"""

n=int(input("nhap so nguyen N: "))
x=float(input("nhap so nguyen x: "))
while n<=0:
    n=int(input("nhap so nguyen N: "))
ms=0
tong=0
for i in range(1,n+1):
    ts=x**i
    ms+= i
    tong+=ts/ms
print("tong la: ",tong)
    