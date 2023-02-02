# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:08:42 2023

@author: Rami
"""

print("Input:")
list1 = input()
list1 = [int(x) for x in list1.split() ] #list1 is now a list of integers
target = int(input())

for i in range(len(list1)):
    num1 = list1[i]
    num2 = target - list1[i] ##the other number
    if(list1.count(num2)>0):
        print(i,list1.index(num2),sep=",")
        break