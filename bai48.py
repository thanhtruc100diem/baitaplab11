# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:12:01 2024

@author: HP
"""
ds=[]
min_t=999
for x in range(1,490):
    for y in range (1,140):
        for z in range(1,109):
            if 2*x+7*y+9*z==979:
                tong=x+y+z
                if tong< min_t:
                    min_t=tong
                    ds=[(x,y,z)]
if ds:
    print("bo nghiem thoa man yeu cau de bai la: ",ds)
                    

