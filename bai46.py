# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:50:26 2024

@author: HP
"""
ds=[]
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x+7*y+9*z==979:
                ds+=[(x,y,z)]
if ds:
    print("bo nghiem: ",ds)
