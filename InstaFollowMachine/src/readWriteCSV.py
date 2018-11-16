import csv
import time
import numpy as np
from numpy import genfromtxt
from io import StringIO

userIndex = 0
userArray = np.array([[],[]])

def readCSVtoArray():

    with open('usernames.csv', mode='r') as usernameCSV:
        userArray = genfromtxt(usernameCSV, delimiter=',', dtype="|U")
        #print(userArray)

    return(userArray)

#####read and return all user names currently on the CSV
def readAllUserNames():

    allNames = userArray[:,1]
    #print(allNames)
    return(allNames)

######Count the number of names (rows) in the CVS
def countUserNames():

    rowCount = np.size(userArray,0) - 1
    #print(rowCount)
    return(rowCount)

######return the name at a specific row
def searchForUserName(rowNumber):

    theName = userArray.item((rowNumber,1))

    return(theName)

######Append CVS with new name at the next available bottom row
def writeNewName(newUserName):
    newRow = newUserName

    with open('usernames.csv', mode='a') as usernameCSV:
        username_writer = csv.writer(usernameCSV, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        username_writer.writerow([[0],[newRow]])

    return
######Run the CSV Checker and print the array
def checkCSV():

    #readCSVtoArray()
    global userArray
    userArray = readCSVtoArray()
    print(userArray)
#    testingArray = readCSVtoArray()
#    print('this is it now: ')
#    print(testingArray)
#    print('These are the names: ')
#    print(readAllUserNames(testingArray))
#    print('This is the length:')
#    print(countUserNames(testingArray))
#    print('the name at possition row five is:')
#    print(searchForUserName(testingArray, 4))
#   print(countUserNames(userArray))
    return(userArray)

userArray = checkCSV()
