# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 00:35:57 2024

@author: HP
"""
import math
n=int(input("nhap so nguyen n: "))
while n<=0:
    n=int(input("nhap lai n: "))
sochinhphuong=math.sqrt(n)
a= int(sochinhphuong)
kq=a*a
if n == kq:
    print("do la so chinh phuong")
else:
    print("do khong phai la so chinh phuong")