from fileinput import *
import os

def addToList(text, listName):
    with open(listName + '.snow', "a") as f:
        f.writelines(text)
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
def getLineContent(line, listName):
    with open(listName + '.snow', "r") as f:
        lines = f.readlines()
    f.close()
    return lines[line]

# print every line but replace ; with \n
def printList(listName):
    with open(listName + '.snow', "r") as f:
        for line in f:
            print(line.replace(";", "\n"))
    f.close()

# get number of lines in list but add 1 of every semicolon
def getLineCount(listName):
    with open(listName + '.snow', "r") as f:
        lines = f.readlines()
    f.close()
    line_count = 0
    for line in lines:
        line_count += line.count(";") + 1
    return line_count
def getLineContent(line_section, listName):
    # Assumes that your line number (for example, "3.2") is a string named `line_section`
    line_number, section_number = line_section.split('.') # Currently both values are str
    line_number = int(line_number)
    section_number = int(section_number)
    with open(listName + '.snow', 'r') as file:
        selected_line = file.readlines()[line_number - 1] # Python lists are 0-indexed, so subtract one from the line number
        selected_section = selected_line.split(";")[section_number - 1]
    # selected_section is the final result
    return selected_section
def deleteLine(lineNumber, listName):
    line = lineNumber
    list = listName
    newText= getLineContent(line, list)
    #replace the text with the output of getLineContent (delete the line)
    with open(listName + '.snow', 'r') as file:
        text = file.read()
    # Delete text and Write
    with open(listName + '.snow', 'w') as file:
        # Delete
        new_text = text.replace(newText, '')
        # Write
        file.write(new_text)
    file.close()