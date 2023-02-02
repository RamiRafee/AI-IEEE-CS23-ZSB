# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:59:46 2023

@author: Rami
"""

dict1 = {
    "A":[20,30,100,49],
    "B":[00,199,201,29],
    "C":[40,90,69,18]
}

varRange = 0
varKey=list(dict1.keys())[0]
for key in dict1:
    temp = max(dict1[key])-min(dict1[key])
    if(temp>varRange):
        varRange = temp
        varKey=key
print (key)