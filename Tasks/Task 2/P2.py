# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:16:50 2023

@author: Rami
"""

# def countEven(array):
#     """
#     before reduction function
#     input :
#         list
#     output:
#         number of even elements in the list
#     """
#     count = 0
#     for i in array:
#         if i %2 ==0:
#             count +=1   
#     return count
if __name__ == "__main__":
    print("input:")
    array = input().split()
    array = [int(x) for x in array]
    
    even = list(filter(lambda i:(i%2 ==0),array))
    
    print("OUTPUT:")
    print(len(even))
    
    
