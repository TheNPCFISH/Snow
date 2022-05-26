"""
SnowForPython

A package for using Snow datastores in python.
"""

__version__ = "0.1"
__author__ = 'NPCFISH'


from fileinput import *
import os

def addToList(text, listName):
    with open(listName + '.snow', "a") as f:
        f.writelines(text)
    f.close()
def lengthOfList(listName):
    line_count = 0
    with open(listName + '.snow', "r") as f:
        for line in f:
            line_count += 1
    f.close()
    return line_count
def printList(listName):
    with open(listName + '.snow', "r") as f:
        for line in f:
            print(line)
    f.close()
def deleteFromList(text, listName):
    with open(listName + '.snow', "r") as f:
        lines = f.readlines()
    f.close()
    with open(listName + '.snow', "w") as f:
        for line in lines:
            if line != text:
                f.write(line)
    f.close()
def clearList(listName):
    with open(listName + '.snow', "w") as f:
        f.truncate()
    f.close()
def deleteList(listName):
    os.remove(listName + '.snow')
def checkIfInList(text, listName):
    with open(listName + '.snow', "r") as f:
        lines = f.readlines()
    f.close()
    for line in lines:
        if line == text + "\n":
            return True
    return False
def deleteLine(lineNumber, listName):
    with open(listName + '.snow', "r") as f:
        lines = f.readlines()
    f.close()
    with open(listName + '.snow', "w") as f:
        for i in range(len(lines)):
            if i != lineNumber:
                f.write(lines[i])
    f.close()
def getLineContent(line, listName):
    with open(listName + '.snow', "r") as f:
        lines = f.readlines()
    f.close()
    return lines[line]