import os
import re
import sys

#Step 0: Check path for files and correct command line calls
# set input and output files
if len(sys.argv) is not 3:
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

#Step 2: Output the dictionary to a file overriding the file if it exists
