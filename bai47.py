# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:06:41 2024

@author: HP
"""

ds=[]
max_t=0
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x+7*y+9*z==979:
                tong=x+y+z
                if tong>max_t:
                    max_t=tong
                    ds=[(x,y,z)]
if ds:
    print("bo nghiem nguyen cua phuong trinh thoa man yeu cau la: ",ds)