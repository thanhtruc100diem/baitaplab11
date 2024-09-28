# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 11:55:55 2024

@author: HP
"""

n=int(input("nhap so nguyen N: "))
while n<=0:
    n=int(input("nhap lai so nguyen N: "))
s=0
for i in range(1,n+1):
    s+= 1/(2*i)
print ("tong la: ",s)