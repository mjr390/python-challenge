# import needed packages
import csv
import os

# create a variable of where the file is located, change for different files
csvpath = os.path.join('..', 'PyPoll', 'election_data_2.csv')

#set counters to 0 and create empty lists
totalVotes = 0
candidates = []
voteCount = []
percentVotes =[]

#open the file reading each line as a new line in csv format
with open(csvpath, newline='') as csvfile:
    #assign the read file to a variable separated by ','
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip over the header line in the data
    headers = next(csvreader)

    #go through each row
    for row in csvreader:
        
        #increment totalVotes by 1 for each line to get the total number of votes
        totalVotes += 1
        #check if a candidate's name has been voted for at least once and add their name to a list
        if row[2] not in candidates:
            candidates.append(row[2])
            voteCount.append(0)   
        
        #increase vote count for each candidate each time they are voted for
        x = len(candidates)
        while x > 0:
            if row[2] == candidates[x-1]:
                 voteCount[x-1] +=  1
            x -= 1         


    #find out which postion has the most votes, 
    #figure out where that position is, assign that to a variable, 
    #then match it up to the correct candidate
    winner = (max(voteCount))
    win = voteCount.index(winner)
    trueWinner = candidates[win]

    #print the results to the console with format lines
    print("ELection Results")
    print("-"*30)
    print("Total Votes: " + str(totalVotes))
    print("-"*30)
    #loop through each candiate for their name, votes, and percent. print these in one line
    z = len(candidates)
    while z > 0:
        print(candidates[z-1] + ": " + str((voteCount[z-1]/totalVotes)*100) + "% (" + str(voteCount[z-1]) + ")")
        z -=1    
    print("-"*30)
    print("Winner: " + trueWinner)
    print("-"*30)    
#Output the rezults to a new file. MUST be a differnet file name from one that already exists   
output_path = os.path.join("..", "PyPoll", "output_2.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    #write the lines in the new file
    csvwriter.writerow(['Election Results', "", ""])
    csvwriter.writerow(['Total Votes:', totalVotes, ""])
    zz = len(candidates)
    while zz > 0:
        csvwriter.writerow([candidates[zz-1], ((voteCount[zz-1]/totalVotes)*100), voteCount[zz-1]])
        zz -= 1
    csvwriter.writerow(['Winner:', trueWinner, ""])    