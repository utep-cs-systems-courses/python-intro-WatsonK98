import os
import re
import sys
import string

#Step 0: Check path for files and correct command line calls
# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

#set Input and Ouptut files
inputFile = sys.argv[1]
outputFile = sys.argv[2]

#If the input file doesn't exist then exit
if not os.path.exists(inputFile):
    print("%s Input file not found." % inputFile)
    exit()

#If the output file doesn't exist then exit
if not os.path.exists(outputFile):
    print("%s Output file not found. Creating..." % outputFile)
    open(outputFile, 'w')
else:
    open(outputFile, 'w')

#Dictionary to accumulate words
wordDiction = {}

#Step 1: Read the file absorbing words into the dictionary
with open(inputFile, 'r') as inputFile:
    text = inputFile.read()

    translator = str.maketrans('','',string.punctuation)
    text = text.translate(translator).lower()

    words = text.split()

    for word in words:
        if word in wordDiction:
            wordDiction[word] += 1
        else:
            wordDiction[word] = 1

sort = sorted(wordDiction.items(), key=lambda x: x[0])


#Step 2: Output the dictionary to a file overriding the file if it exists
with open(outputFile, 'w') as output:
    for word in wordDiction:
        count = wordDiction[word]
        output.write(f"{word} {count}\n")