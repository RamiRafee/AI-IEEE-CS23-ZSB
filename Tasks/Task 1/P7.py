# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 15:01:31 2023

@author: Rami
"""

print("Input:")
list1 = input()
list1 = [int(x) for x in list1.split() ] #list1 is now a list of integers

target = int(input())

for i in range(target):
    list1.insert(0, list1[len(list1)-1])
    list1.pop()

print("Output:",list1,sep="\n")