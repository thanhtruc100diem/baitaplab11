# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 11:41:15 2024

@author: HP
"""

n=int(input("nhap so nguyen le n: "))
while n<=0:
    n=int(input("nhap lai so nguyen le N:"))
s=1
for i in range (1, n+1):
    s *=i
print("tong la: ",s)
    