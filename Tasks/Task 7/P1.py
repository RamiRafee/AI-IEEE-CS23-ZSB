# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:28:17 2023

@author: Rami
"""



"""
getting Input
"""
import numpy as np

print("Input:")

flipNum = 0
Type = ""
appearance = 0
probability = 0.0
probabilityOpposite = 0.0

while (1):
    try:
        try:
            if(not flipNum):
                flipNum = int(input("The number of flips: "))
            
        except ValueError:
            
            print("please enter a valid number")
            continue
        
            
        
        if (Type not in ["head","tail"]):
            Type = input("Head or Tail?").lower()
            print("enter a valid type")
            continue
        
        try:
            
            
            if(not appearance):
                appearance = int(input("The number of {} appearance: ".format(Type)))
            if(not probability):
                probability = float(input("The probability of {} (< 1): ".format(Type)))
                probabilityOpposite = 1 - probability
                
                
        except ValueError:
            print("please enter  valid numbers")
            continue
        
    except KeyboardInterrupt:
        
        print("Ended")
        raise SystemExit(0)
    break
        
"""
Truth Table:
    creating a complete Dynamic Truth Table
"""

TruthTable = [] # a 2^flipnumber X flipnumber LIST eg: if flip number == 3
                # it will be a 8X3 LIST

for i in range(2**flipNum): 
    
    TruthTable.append(list())
    
    for j in range(flipNum):
        
        TruthTable[i].append ("Empty")
        

TruthTable = np.array(TruthTable) #dealing with column in numpy is much easier
   

for i in range(flipNum):
    
    changingNum = 2**i #the H or T change every changinNum
    
    tempList = TruthTable[:,flipNum - 1 - i] #tempList containing every column
    
    for j in range(0,len(tempList),2 * changingNum): #setting H every changinNum
        
        
        for k in range(j,j+ (changingNum)): #setting H for chaningNum times
            tempList[k] = "H"
    
    for j in range(changingNum,len(tempList),2 * changingNum): #setting T every changinNum
        
        
        for k in range(j,j+ (changingNum)): #setting T for chaningNum times
            tempList[k] = "T"
            
     
            
TruthTable = list(TruthTable)  


"""

getting the count of rows with the required appearance of the specified Type

getting the rowProbability of the probabilities for the specified row
"""        
rowCount = 0

rowProbability = 1

for i in range(len(TruthTable)):
    
    TruthTable[i] = list(TruthTable[i])
    if (TruthTable[i].count(Type[0].upper()) == appearance):
        rowCount += 1
        
        if ( rowProbability == 1): #if rowProbability doen't equal 1 calculate the rowProbability for the row
            
            for j in TruthTable[i]:
                if j == Type[0].upper():
                    rowProbability *= probability
                else :
                    rowProbability *= probabilityOpposite
            
            
      
# answer = rowCount * (probability*appearance * probabilityOpposite* (flipNum - appearance))   
answer  = rowCount * rowProbability
print("OUTPUT:")
print (f"The answer is: {answer:.3f}")

print("THE TRUTH TABLE IS --->")
print(np.array(TruthTable))


    
        

        