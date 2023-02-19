# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:31:25 2023

@author: Rami
"""

def Q(nslst: list):
    """
    

    Parameters
    ----------
    nslst : not sorted list
        the list from which we will get the 3 quartiles.

    Returns
    -------
    Q : list
        List containing Q1,Q2,Q3.

    """
    Q = []
    n = len(nslst)
    lst = nslst.copy()
    lst.sort()
    half = n//2
    quartile1Int = (n)//4
    quartile2Int = 3*(n)//4
    
    if(n %2 ==0 and n>0):
        Q.append((lst[quartile1Int] + lst[quartile1Int-1])/2)
        Q.append((lst[half] + lst[half - 1])/2)
        Q.append((lst[quartile2Int] + lst[quartile2Int-1])/2)
    elif (n %2 !=0):
        Q1 = int(lst[quartile1Int])
        Q2 = int(lst[half])
        Q3 = int(lst[quartile2Int])
        Q.append(Q1)
        Q.append(Q2)
        Q.append(Q3)
    return Q


def fiveNumberSummary(nslst:list, Q):
    """
    

    Parameters
    ----------
    nslst : not sorted list
        the list from which we will get the minimum , 3 quartiles and maximum.
    Q : function
        function that returns the 3 quartiles.

    Prints
    -------
    The 5 number Summary

    """
    minimum = min(nslst)
    maximum = max(nslst)
    Q = Q(nslst)
    Q1 = Q[0]
    Q2=Q[1]
    Q3 = Q[2]
    
    print("min: {}\nQ1: {}\nQ2: {}\nQ3: {}\nmax: {}".format(minimum,Q1,Q2,Q3,maximum))
    numberSummary = {'min':minimum,'Q1':Q1,'Q2':Q2,'Q3':Q3,'max':maximum}
    return numberSummary

def spread(numberSummary):
    """
    

    Parameters
    ----------
    numberSummary : dictionary
        dict that has the 5 number summary.

    Prints
    -------
    the Range and the IQR

    """
    listRange = numberSummary['max'] - numberSummary['min']
    IQR = numberSummary['Q3'] - numberSummary['Q1']
    print("range: {}\nIQR: {}".format(listRange,IQR))
    
def variance(nslst):
    """
    Note : assumed input is *population*

    Parameters
    ----------
    nslst : list
        not sorted list .

    Prints
    -------
    The variance and standard deviation (population).

    """
    mean = sum(nslst)/len(nslst)
    variance= 0
    for i in nslst:
        variance += (i-mean)**2
    variance = variance/(len(nslst) )
    standardDeviation = variance **0.5
    print("Variance:%0.3f"%(variance))
    print("Standard deviation:%0.3f"%(standardDeviation))

print("Input:")
lst=[]
while True:
    try:
        splitted = input().split()
        lst = [float(x) for x in splitted]
        break
    except ValueError:
        print("please enter only numbers")
    except KeyboardInterrupt:
        print("Ended")
        break
if(lst):
    print("\nOutput:")
    numberSummary =  fiveNumberSummary(lst, Q)
    spread(numberSummary)
    variance(lst)

