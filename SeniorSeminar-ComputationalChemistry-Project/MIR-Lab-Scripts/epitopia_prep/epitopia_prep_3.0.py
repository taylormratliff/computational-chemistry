'''
**** Title: Epitopia Prep v3.0
**** Author: Colin Welsh
**** Date: 25 July 2017                        
**** Purpose: Converts a minimized file from Chimera into a file that is compatible
****          for use with epitopia.
'''

import os


def find_files(fileNames,fileRoot):
    fileDirs = {}
    for dirname,subdir,file in os.walk(fileRoot):
        for name in file:
            if name in fileNames:
                fileDirs[name] = os.path.join(dirname,name)
    return fileDirs

def read_file_list(infile):
    fileNames = []
    for line in infile:
        line = line.rstrip('\n')
        fileNames.append(line)
    return fileNames

def batch_processing():
    fileRoot = os.getcwd()
    print("1: Enter filenames individually\n2: Enter filenames in a single .txt file\n3: Exit")
    batchOption = int(input('Enter choice: '))
    cont = False
    if batchOption == 1:
        fileNames = []
        print('Enter a filename. Enter "0" to exit.')
        filename = input('Enter filename: ')
        while filename != '0':
            fileNames.append(filename)
            filename = input('Enter filename: ')
            cont = True
    elif batchOption == 2:
        fileListName = input('Enter batch list file: ')
        fileList = open(fileListName, 'r')
        fileNames = read_file_list(fileList)
        cont = True
    if cont == True:
        fileDirs = find_files(fileNames,fileRoot)
        return fileDirs, fileNames
    

### Parameters: infileName, the name of the .pdb file to be converted
###
### Returns: outfileName, the name of the temp file with no repeating sequence nums
###
### Purpose: changes the loc numbers of the amino acids if there is overlap
def pre_check(infileName):
    infile = open(infileName, 'r')
    outfileName = infileName.rstrip('.pdb') + "_tempfile.pdb"
    outfile = open(outfileName, 'w')
    prevNum = 'ABC'
    cnt = 0
    for line in infile:
        if line.startswith('ATOM'):
            num = line[23:26]
            if num != prevNum:
                cnt += 1
                if cnt < 10:
                    fixedNum = "  " + str(cnt)
                elif cnt >= 10 and cnt < 100:
                    fixedNum = " " + str(cnt)
                else:
                    fixedNum = str(cnt)
            prevNum = num
            outfile.write(line[:23])
            outfile.write(fixedNum)
            outfile.write(line[26:])
            outfile.write('\n')

    outfile.close()
    return outfileName
            
    
### Parameters: infileName, name of the .pdb file to be converted
###
### Returns: aminoList, a dictionary of the amino acids matched with their loc number
### largest, the largest loc number
###
### Purpose: creates a dictionary to be used in creating the file header
def make_amino_list(infileName):
    infile = open(infileName,'r')
    aminoList = {}
    largest = 0
    for line in infile:
        if line.startswith('ATOM'):
            loc = line[22:26]
            loc = loc.lstrip()
            loc = int(loc)
            aminoAcid = line[17:20]
            if loc > largest:
                largest = loc
            if loc not in aminoList:
                aminoList[loc] = aminoAcid        
    infile.close()
    return aminoList,largest


### Parameters: outfile, the file to be submitted to Epitopia
### aminoList, a dictionary containing all unique AA/loc numbers from original .pdb
### largest, largest loc number in original .pdb
###
### Returns: None
###
### Purpose: writes the file header required by Epitopia
def write_seqres(outfile,aminoList,largest):
    k = 1
    if largest % 13 == 0:
        numRows = largest // 13
    else:
        numRows = (largest // 13) + 1
    if largest < 10:
        spacer = "    "
    elif largest > 9 and largest < 100:
        spacer = '   '
    elif largest > 99 and largest < 1000:
        spacer = '  '
    if largest > 999:
        spacer = ' '
    for i in range(1,numRows+1,1):
        multiplier = (i - 1) * 13
        if i < 10:
            header = "SEQRES   " + str(i) + " A" + spacer + str(largest) + "  "
        elif i >= 10 and i < 100:
            header = "SEQRES  " + str(i) + " A" + spacer + str(largest) + "  "
        else:
            header = "SEQRES " + str(i) + " A" + spacer + str(largest) + "  "
        outfile.write(header)
        for k in range(1,14,1):
            loc = k + multiplier
            if loc in aminoList:
                amino = aminoList[loc]
                outfile.write(amino)
                outfile.write(' ')
        outfile.write('\n')
            

### Parameters: outfile, the file to be submitted to epitopia
### infileName, the name of the file that is the original .pdb (or pre-checked file, if
### appropriate)
###
### Returns: none
###
### Purpose: writes the rest of the original .pdb
def write_bulk(outfile,infileName):
    infile = open(infileName,'r')
    for line in infile:
        if line.startswith('ATOM') or line.startswith('END'):
            outfile.write(line)

def main():
    batchProcessing = False
    batchOption = input('Batch processing? (y/n): ')
    if batchOption == 'y' or batchOption == 'Y':
        batchProcessing = True
    if batchProcessing:
        fileList,fileNames = batch_processing()
        doPreCheck = input('Precheck files? (Y/N): ')
        for obj in fileNames:
            #infileName = obj
            outfileName = "epitopia_" + obj
            outfile = open(outfileName, 'w')
            if doPreCheck == 'Y' or doPreCheck == 'y':
                infileName = pre_check(fileList[obj])
            aminoList,largest = make_amino_list(fileList[obj])
            write_seqres(outfile,aminoList,largest)
            write_bulk(outfile,fileList[obj])
            outfile.close()
            if doPreCheck == 'Y' or doPreCheck == 'y':
                os.remove(fileList[obj])
    else:
        infileName = input('Enter file name to be prepped for epitopia (include .pdb): ')
        outfileName = "epitopia_" + infileName
        outfile = open(outfileName,'w')
        doPreCheck = input('Precheck files? (Y/N): ')
        if doPreCheck == 'Y' or doPreCheck == 'y':
            infileName = pre_check(infileName)
        aminoList,largest = make_amino_list(infileName)
        write_seqres(outfile,aminoList,largest)
        write_bulk(outfile,infileName)
        outfile.close()
        if doPreCheck == 'Y' or doPreCheck == 'y':
            os.remove(infileName)
    
main()
