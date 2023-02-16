# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:50:11 2023

@author: Rami
"""
def mode(lst : list):
    """
    

    Parameters
    ----------
    lst : list
        The list that we want to find the mode for.

    Returns
    -------
    dic : dictionary
        dictionary that contains the modes as keys.

    """
    dic = {lst[0]:lst.count(lst[0])}
    for i in lst:
        if (lst.count(i)> list(dic.values())[0]):
            dic.clear()
            dic[i] = lst.count(i)
        elif (lst.count(i)== list(dic.values())[0] and i not in (dic.keys())):
            dic[i] = lst.count(i)
    if(len(dic.keys())*list(dic.values())[0] == len(lst)):
        dic.clear()
    return dic


def median(nslst: list):
    """
    

    Parameters
    ----------
    uslst : list
        The list that we want to find the median for.
        ns stands for notsorted
    Returns
    -------
    The median.

    """
    median = 0
    n = len(nslst)
    lst = nslst.copy()
    lst.sort()
    if(n %2 ==0 and n>0):
        temp = n//2
        median = (lst[temp] + lst[temp - 1])/2
    elif (n %2 !=0):
        median = lst[n//2]
    return median

def mean(lst: list)->float:
    """
    

    Parameters
    ----------
    lst : list
        The list that we want to find the mean for.

    Returns
    -------
    float
        the mean of the list.

    """
    s = 0
    for i in  lst:
        s += i
    if(len(lst)!= 0):
        mean = s/len(lst)
        return mean
    else :
        return 0



print("Input:")

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
    print("Mean :%0.3f"%(mean(lst)))
    print("Median :%0.2f"%(median(lst)))
    print("Mode :{}".format(list(mode(lst).keys())))