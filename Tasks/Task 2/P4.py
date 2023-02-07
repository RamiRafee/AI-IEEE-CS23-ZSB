# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:15:22 2023

@author: Rami
"""
if __name__ == "__main__":
    try:
        file = open('grades.txt', 'r')
    except:
        print("file not found")
    file.readline()
    users = dict()
    oldestId=1
    highestId=1
    
    for line in file:
        array = line.split()
        try:
            tempId = int(array[0])
            tempName = array[1]
            tempScore = int(array[2])
            tempBirth = int(array[4])
            tempGender = array[6]
            if tempGender == 'm':
                tempGender = "Male"
            else:
                tempGender = "Female"
            users[tempId]={'name':tempName,
                             'score':tempScore,
                             'birthyear':tempBirth,
                             'gender':tempGender
                             }
        except:
            continue
        if(users[tempId]['birthyear'] < users[oldestId]['birthyear']):
            oldestId = tempId
        if(users[tempId]['score'] < users[highestId]['score']):
            highestId = tempId
    
    
    avg = 0
    usersValues = users.values()
    for x in usersValues:
        avg += x['score']
    avg = avg/len(usersValues)
   
    print ("The ID of the oldest user IS ->{}".format(oldestId))
    print("The Average Score is -> {}".format(avg))
    print("The sex of the user with the highest Score is ->{}".format(users[highestId]['gender']))
    
