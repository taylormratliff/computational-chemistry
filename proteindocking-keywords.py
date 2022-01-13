#A.2.6 KEYWORDS-WRITE.PY SCRIPT
import string 
import os
import sys

# This will only work for file names ending with .#.mo.out or the like, where
#the file number is in the 1st from last position in the filename.

inFile = sys.argv[1]
inParts = string.split(inFile, ".")
#print inParts
print "\n"
print ("%s is running." %inFile)
print "\n"
outName = inParts[0]
outName = outName+"-proteins.pdb"
	
print "\n"
print " inserting keywords HEADER \n"

input = open('%s' %inFile,'r')

#input = open(Benz.svs.mo.out, 'r')
outFile = open('%s' %outName,'a')
#outFile = open(test.keywords.mo.dat, 'a')
outFile.write("HEADER rec.pdb \n")
outFile.write("REMARK original generated coordinate pdb file \n")
	#outFile = open(Benz.chg, 'a')


infile = open('%s' %inFile,'r')
infile.readline()
infile.readline()
for i in range (1, 1000000):
	line = infile.readline()
	outFile.write(line)
