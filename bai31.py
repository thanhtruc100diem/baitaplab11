# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 00:14:35 2024

@author: HP
"""

a=int(input("nhap do dai canh thu nhat: "))
b=int(input("nhap do dai canh thu hai: "))
c=int(input("nhap do dai canh thu ba: "))
if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        print("do la tam giac deu")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("do la tam giac can")
    elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2 +c**2== b**2:
        print("do la tam giac vuong")
    else:
        print("do la tam giac thuong")
else:
    print("cac so da nhap khong tao thanh mot tam giac")
        