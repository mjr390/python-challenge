# Test to see if this uploads
import csv
import os

csvpath = os.path.join('..', 'PyPoll', 'election_data_1.csv')

totalVotes = 0
candidates = []
voteCount = []
percentVotes =[]

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    headers = next(csvreader)

    for row in csvreader:
        
        totalVotes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            voteCount.append(0)   
        
        x = len(candidates)
        
        while x > 0:
            
            # print("H")
            if row[2] == candidates[x-1]:
                 voteCount[x-1] +=  1
            # print("y=2")
            x -= 1         


    


    winner = (max(voteCount))
    win = voteCount.index(winner)
    trueWinner = candidates[win]

 


    print("ELection Results")
    print("-"*30)
    print("Total Votes: " + str(totalVotes))
    print("-"*30)
    z = len(candidates)
    while z > 0:
        print(candidates[z-1] + ": " + str((voteCount[z-1]/totalVotes)*100) + "% (" + str(voteCount[z-1]) + ")")
        z -=1    
    print("-"*30)
    print("Winner: " + trueWinner)
    print("-"*30)    
   