# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 11:38:29 2024

@author: HP
"""

n=int(input("nhap so nguyen nguyen duong chan N: "))
while n <=0:
    n=int(input("nhap lai so nguyen duong chan N: "))
s=0
for i in range(2,n+1,2):
    s+= i
print ("tong la: ",s)
