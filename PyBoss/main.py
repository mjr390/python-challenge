#import needed packages
import os
import csv
from datetime import datetime

# create a variable of where the file is located, change () for different files
csvpath = os.path.join('..', 'PyBoss', 'employee_data2.csv')

#Create lists to populate with altered data
splitNames = []
firstNames = []
lastNames = []
DOB = []
SSNall = []
ID = []
stateApp = []
#use a dictionary to convert state names to appreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


#open the file reading each line as a new line in csv format
with open(csvpath, newline='') as csvfile:
    #assign the read file to a variable separated by ','
    csvreader = csv.reader(csvfile, delimiter=",")
     #skip over the header line in the data
    headers = next(csvreader)
    #go through each row to convert data to new format
    for row in csvreader:
        
        #create a new list with first and last name as sererate values
        splitNames.append(row[1].split(" "))
        #add the first names to the firstNames list and the last names to lastNames list
        firstNames.append(splitNames[0][0])
        lastNames.append(splitNames[0][1])
        #remove the current first position name from spiltNames to do the next name the next loop
        splitNames.pop(0)
        
        #change DOB from yyyy/mm/dd to mm/dd/yyyy
        DOB.append(datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'))
        
        #* out numbers in the SSN by converting it to a list
        secretSSN = list(row[3])
        #changing the desiered locations to stars
        secretSSN[0:3] = '***'
        secretSSN[4:6] = "**"
        #join the list back together
        secretSSNstr = ''.join(secretSSN)
        #assign the new list to a variable
        SSNall.append(secretSSNstr)
        
        #create a variable for the ID's as is
        ID.append(row[0])

        #convert the states to their proper appreviations
        stateApp.append(us_state_abbrev[row[4]])

        #zip the new formats together
        newFormat = zip(ID, firstNames, lastNames, DOB, SSNall, stateApp)
        

#output a new file with the converted info. in () put the location and file name, cannot be an existing file name
output_file = os.path.join("output_2.csv")

#write the new file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    #write a row for the headers
    writer.writerow(["Employee ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    #write the rest of the rows using the variable for the zip
    writer.writerows(newFormat)

        



       



#print(new)
#print(lastNames)
#print(DOB)
#print(SSNall)
#print(ID)
#print(stateApp)

