import csv
import os
import re

# senCount = 0

filepath = open("../PyParagraph/paragraph_1.txt", "r")
# with open(filepath, newline='.') as csvfile:
x = filepath.read()
#csv.filepath()
#filepath.split('.')
wordCount = len(x.split())
print(wordCount)
sentenceCount = len(x.split('.'))
print(sentenceCount)
avgSentenceLength = wordCount/sentenceCount
print(avgSentenceLength)







#     for line in file:
#         # print(len(line))
#         #line.split(" ")
#         filereader = (file, " ")
#         for x in filereader:
#             senCount += 1
#     print(senCount)        



# filepath = os.path.join('..', 'PyParagraph', 'paragraph_1.txt')

# senCount = 0
# #open the file reading each line as a new line in csv format
# with open(filepath, newline='') as afile:
#     #assign the read file to a variable separated by ','
#     filereader = (afile, ".")
#     print(filereader)
#     #csv.reader(csvfile, delimiter=".")
  
# #     x = ' '
#     for x in csvreader:
#         senCount += 1#


# print(senCount)        