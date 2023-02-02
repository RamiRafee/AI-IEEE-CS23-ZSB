# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:52:56 2023

@author: Rami
"""

print("Input:")
list1 = input()
list1 = [int(x) for x in list1.split() ] #list1 is now a list of integers

symm= True

for i in range(len(list1)):
    if(list1[i]!=list1[len(list1)-1-i]):
        symm=False
    
print(symm)