#import needed packages
import csv
import os
import re

# create a variable of where the file is located, change for different files
filepath = open("../PyParagraph/paragraph_2.txt", "r")

#create a variable to read the file
readText = filepath.read()

#find out the number of words by spliting the text based on spaces and assigning to a var
wordCount = len(readText.split())
#print(wordCount)

#find the number of sentences by spliting the text based on "." and assigning to a var
sentenceCount = len(readText.split('.'))
#print(sentenceCount)

#find the average number of words in a sentence by divding wordCount by sentenceCount and assign the result to a var
avgSentenceLength = wordCount/sentenceCount
#print(avgSentenceLength)

#find the total number of letters by creating a variable and setting it to 0
letterCount = 0

#create a list of every letter to check if a character in the text is a letter
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
for char in readText:
    #if it is, add to letterCount to keep a running total of how many letter there are
    if char in alphabet:
        letterCount += 1
#print(letterCount)
#find the average letters per word by divding the total number of letters by the total words. Assign the result to a variable
avgLetterCount = letterCount/wordCount
#print(avgLetterCount)  


#print the results to the console with some formatting
print("Paragraph Analysis")
print("-"*30)
print("Approximate Word Count: " + str(wordCount))
print("Approximate Sentence Count: " + str(sentenceCount))
print("Average Letter Count: " + str(avgLetterCount))
print("Average Sentence Length: " + str(avgSentenceLength))      

#Output the rezults to a new CSV file. 
#MUST be a differnet file name from one that already exists   
output_path = os.path.join("..", "PyParagraph", "output_2.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    #write the lines in the new file
    csvwriter.writerow(["Paragraph Analysis", ""])
    csvwriter.writerow(["Approximate Word Count: ", str(wordCount)])
    csvwriter.writerow(["Approximate Sentence Count: ", str(sentenceCount)])
    csvwriter.writerow(["Average Letter Count: ", str(avgLetterCount)])
    csvwriter.writerow(["Average Sentence Length: ", str(avgSentenceLength)])