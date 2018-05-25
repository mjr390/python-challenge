import csv
import os
import re



filepath = open("../PyParagraph/paragraph_1.txt", "r")

x = filepath.read()

wordCount = len(x.split())
print(wordCount)

sentenceCount = len(x.split('.'))
print(sentenceCount)

avgSentenceLength = wordCount/sentenceCount
print(avgSentenceLength)

# print(totalcom)
letterCount = 0
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
for char in x:
    if char in alphabet:
        letterCount += 1
#print(letterCount)
avgLetterCount = letterCount/wordCount
print(avgLetterCount)        
