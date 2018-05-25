import csv
import os
import re



filepath = open("../PyParagraph/paragraph_2.txt", "r")

x = filepath.read()

wordCount = len(x.split())
#print(wordCount)

sentenceCount = len(x.split('.'))
#print(sentenceCount)

avgSentenceLength = wordCount/sentenceCount
#print(avgSentenceLength)

# print(totalcom)
letterCount = 0
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
for char in x:
    if char in alphabet:
        letterCount += 1
#print(letterCount)
avgLetterCount = letterCount/wordCount
#print(avgLetterCount)  

print("Paragraph Analysis")
print("-"*30)
print("Approximate Word Count: " + str(wordCount))
print("Approximate Sentence Count: " + str(sentenceCount))
print("Average Letter Count: " + str(avgLetterCount))
print("Average Sentence Length: " + str(avgSentenceLength))      


output_path = os.path.join("..", "PyParagraph", "output_2.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Paragraph Analysis", ""])
    csvwriter.writerow(["Approximate Word Count: ", str(wordCount)])
    csvwriter.writerow(["Approximate Sentence Count: ", str(sentenceCount)])
    csvwriter.writerow(["Average Letter Count: ", str(avgLetterCount)])
    csvwriter.writerow(["Average Sentence Length: ", str(avgSentenceLength)])