# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:34:18 2023

@author: Rami
"""

if __name__ == "__main__":
    print("input:")
    while True:
        try:
            array = input().split()
            array = [int(x) for x in array]
            break
        except:
            print("THE LIST MUST BE INTEGERS ONLY")
        finally:
            print("Attempt Was Recorded")
    print("Input was Successful")
    
    
    
    array.sort()
    maxSub=[array[len(array)-1]]
    minSub=[array[0]]
    
    minSum=array[0]
    maxSum=array[len(array)-1]
    for i in range(len(array)):
        ##
        if(array[i] + maxSum > maxSum and array[i] != maxSub[0]):
            maxSum = array[i] + maxSum
            maxSub.append(array[i])
            
        ## to handle the [Len(sublist) > 1]
        # elif(array[i] + maxSum > maxSum and array[i] == maxSub[0] and len(maxSub)==1):
        #     maxSum = array[i - 1] + maxSum
        #     maxSub.append(array[i-1])
            
        ##
        
        elif(array[i] + minSum< minSum and array[i] != minSub[0]):
            minSum = array[i] + minSum
            minSub.append(array[i])
            
        ## to handle the [Len(sublist) > 1]
        # elif(array[i] + minSum< minSum and array[i] == minSub[0] and len(minSub)==1):
        #     minSum = array[i+1] + minSum
        #     minSub.append(array[i+1])
        
        ##to handle the [Len(sublist) > 1]
    if(len(maxSub) ==1 ):
        maxSub.append(array[len(array)-2])
        maxSum = array[len(array)-2] + maxSum
    if(len(minSub) ==1 ):
        minSub.append(array[1])
        minSum = array[1] + minSum
    
    print("OUTPUT:")
    print(maxSub," ({})".format(maxSum))
    print(minSub," ({})".format(minSum))
        
    
    