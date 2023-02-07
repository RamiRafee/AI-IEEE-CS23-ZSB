# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:44:30 2023

@author: Rami
"""
from P4 import users
def write(filename,users):
    file = open(filename, 'w')
    for user in users.keys():
        string = "{} {} - {}\n".format(user,users[user]['name'],users[user]['birthyear'])
        file.write(string)
    file.close()
if __name__ == "__main__":
    write("filtered.txt", users)