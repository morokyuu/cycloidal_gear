# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 08:30:07 2023

@author: square
"""

for a in range(10,61):
    for b in range(10,61):
        c = (a+b)/b
        # print(c)
        if c.is_integer():
            print(f"{a},{b} __ {c}")


