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

