# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 00:01:24 2024

@author: HP
"""

n=int(input("nhap so nguyen duong n: "))
while n <=0 :
    n=int(input("nhap lai so nguyen n: "))
tong=0
for i in str(n):
    tong+= int(i)
print (tong)