#import needed packages
import os
import csv
from datetime import datetime

# create a variable of where the file is located, change for different files
csvpath = os.path.join('..', 'PyBoss', 'employee_data1.csv')

splitNames = []
firstNames = []
lastNames = []
DOB = []
SSNall = []
ID = []

#open the file reading each line as a new line in csv format
with open(csvpath, newline='') as csvfile:
    #assign the read file to a variable separated by ','
    csvreader = csv.reader(csvfile, delimiter=",")
     #skip over the header line in the data
    headers = next(csvreader)

    for row in csvreader:
        splitNames.append(row[1].split(" "))
        firstNames.append(splitNames[0][0])
        lastNames.append(splitNames[0][1])
        splitNames.pop(0)
        DOB.append(datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'))
        secretSSN = list(row[3])
        secretSSN[0:3] = '***'
        secretSSN[4:6] = "**"
        secretSSNstr = ''.join(secretSSN)
        SSNall.append(secretSSNstr)
        ID.append(row[0])





#print(lastNames)
#print(DOB)
#print(SSNall)
#print(ID)

