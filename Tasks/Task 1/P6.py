# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:46:24 2023

@author: Rami
"""
print("Input:")
persons = input()
persons +=","+ input()

persons = persons.split(",")

keys = [x.split(":")[0] for x in persons]
values = [int(x.split(":")[1]) for x in persons]

dict1 = dict(zip(keys,values))

print(dict1)

