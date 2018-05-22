#import needed packages
import os
import csv

# create a variable of where the file is located, change for different files
csvpath = os.path.join('..', 'PyBank', 'budget_data_2.csv')

#set counters to 0 and create empty lists
months = 0
totalRev = 0
monthRev = []
change = []
monthChange = []
date = []

#open the file reading each line as a new line in csv format
with open(csvpath, newline='') as csvfile:
    #assign the read file to a variable separated by ','
    csvreader = csv.reader(csvfile, delimiter=",")
     #skip over the header line in the data
    headers = next(csvreader)

    #go through each row, increaseing the months by 1 each time, 
    #totalRev by each value, add each months reveue to a list and add each date to a list
    for row in csvreader:
        months += 1
        totalRev += int(row[1])
        monthRev.append(int(row[1]))
        date.append(row[0])
        
    #create anouther var with the values as the monthRev list
    monthChange = monthRev
    #set a variable equal to the count of months to use in a loop
    x = months
    # print(monthRev)
    #loop through each month finding the change from each one
    #remove the searched row and decrease x by 1 each time to go to the next row
    while x > 1:
      
        change.append(monthChange[1]-monthChange[0])
   
        monthChange.pop(0)
        x -= 1

    
    # print(monthChange)
    
    # print(totalRev)
    # #print(months)
    # print((sum(monthRev)/len(monthRev)))
    # print(change)
    # print((sum(change)/len(change))) 

    #calculate the revenue change
    avgRevCh = (sum(change)/len(change))
    #find the greatest revenue increase by finding the highest revenue value
    #then finds it's position and set to a variable
    #use this variable as an index to find the month where the greatest change occured
    #repeat for the greatest decrease
    greatRev = max(change)
    greatMonthPos = change.index(greatRev)
    greatMonth =  date[greatMonthPos+1]
    revDec = min(change)
    revDecPos = change.index(revDec)
    worstMonth = date[revDecPos+1]

    #print(greatMonth)

    # print(revDec)

    # print(greatRev)

    #print the findings to the console
    print("Financial Analysis")
    print("-"*30)
    print("Total Months: " + str(months))
    print("Total Revenue: $" + str(totalRev))
    print("Average Revenue Change: $" + str(avgRevCh))
    print("Greatest Increase in Revenue: " + greatMonth + " ($" + str(greatRev) + ")")
    print("Greatest Decrease in Revenue: " + worstMonth + " ($" + str(revDec) + ")")

#Output the rezults to a new file. 
#MUST be a differnet file name from one that already exists   
output_path = os.path.join("..", "PyBank", "output_2.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    #write the lines in the new file
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Total Months:', months])
    csvwriter.writerow(['Total Revenue: ', totalRev])
    csvwriter.writerow(['Average Revenus Change: ', avgRevCh])
    csvwriter.writerow(['Greatest Increase in Revenue:', greatMonth, greatRev])
    csvwriter.writerow(['Greatest Decrease in Revenue: ', worstMonth, revDec])



        