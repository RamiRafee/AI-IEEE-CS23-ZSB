# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:31:31 2023

@author: Rami
"""
print("Input:")
list1 = input()
list1 = [int(x) for x in list1.split() ] #list1 is now a list of integers

list1 = set(list1)
list1 = list(list1)##to remove duplicates

list1.sort()

if(len(list1)>1):
    print(list1[len(list1)-2])##second largest
    print(list1[1])##second smallest
else:
    print(list1[0])
    print(list1[0])

