# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 01:01:56 2024

@author: HP
"""

n=int(input("nhap so nguyen n: "))
while n<=0:
    n=int(input("nhap lai so nguyen n: "))
if n<=2:
    print("do khong phai so nguyen to")
else:
    for i in range(2,n):
        if n%i==0:
            print("do khong phai so nguyen to")
            break
    else:
        print("do la so nguyen to")