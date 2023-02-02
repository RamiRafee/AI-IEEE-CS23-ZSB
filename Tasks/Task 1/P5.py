# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:18:42 2023

@author: Rami
"""

print("Input:")
stringList = input().split()

list1=list()
list2=list()

for i in range(len(stringList)):
    wordLength = len(stringList[i])
    halfLength = (wordLength/2)
    ##to handle the round issue
    if(halfLength> wordLength//2):
        halfLength = (wordLength//2) +1
    halfLength = int(halfLength)
    
    firstHalf = ""
    secondHalf=""
    for j in range(halfLength):
        firstHalf = firstHalf + stringList[i][j]
    for j in range(halfLength,wordLength):
        secondHalf = secondHalf + stringList[i][j]
    list1.append(firstHalf)
    list2.append(secondHalf)

print("Output:",list1,list2,sep="\n")