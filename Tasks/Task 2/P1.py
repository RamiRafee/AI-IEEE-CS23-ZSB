# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 08:57:24 2023

@author: Rami
"""

def sortList(array):
    """
    function to sort a list
    input: list
    output: sorted list
    the sorting algorithm is inserion
    """
    for i in range(1, len(array)):
 
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j] :
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key
def firstLastAppearance(array,target):
    """
    function to output the first and last appearance of a target
    in a sorted list.
    input:
        array->sorted list
        target-> element to output its first and last appearance
    output:
        first and last appearance of the target
    
    """
    found = False
    firstLast=list()
    for i in range(len(array)):
        if (array[i] == target and not found):
            firstLast.append(i)
            found = True
        elif(array[i] != target and found):
            firstLast.append(i-1)
    return firstLast

if __name__ == "__main__":
    print("input:")
    array = input().split()
    array = [int(x) for x in array]
    target = int(input())
    sortList(array)
    firstAndLast= firstLastAppearance(array, target)
    print("OUTPUT:")
    print(firstAndLast[0],firstAndLast[1])

