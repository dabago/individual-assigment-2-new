#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 21:55:08 2018

@author: David
"""

#%%

# Adding bubble sort

def bubble(lst):
    for j in range(0, len(lst) - 1):
        for i in range(0, len(lst) - j - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                
#%%
                
                
