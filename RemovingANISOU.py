
#A.2.20 SVS-PDB-FILENAME-EXCHANGE.PY
#READ.line.py separate lines
#This program reads separate lines

import string 
import os
import sys

# This will only work for file names ending with .#.mo.out or the like, where
#the file number is in the 1st from last position in the filename.

print " \n "
print "Removing ANSIOU lines"
print "\n"


#inFile = "result_001.pdb"
inFile = sys.argv[1]
print inFile
inParts = string.split(inFile,".")
print inParts
outParts = inParts[0]
#newparts = string.split(outParts, ".")
#print newparts
#lastparts = newparts[0]
#print lastparts
#print ("%s is running." %inFile)
outName = outParts+"-prepfile.pdb"
print outName	

input = open('%s' %inFile,'r')
# #input = open(Prepare-inputfile.pdb,'r')
#outFile = open("Prepare-input-file.pdb",'a')
# 
#input = open('%s' %inFile,'r')
outFile = open('%s' %outName,'a')

def main():
	

 	for i in range (1, 100000):
 			line = input.readline()
 			if len(line) < 82:
  				if "ATOM"in line:
  				    line = input.readline()					
  				outFile.write(line)
  					
 					#print "Found it"