'''
*** ROSIE File Preparer v3.0
*** Author: Colin Welsh
*** Date Created: 26 July 2017
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

    
def matchChain(line,chain):
    if line[21] == chain:
        return True
    else:
        return False

    
def writeRecChains(recChains,infile,outfile):
    for item in recChains:
        for line in infile:
            if line.startswith('ATOM') and matchChain(line,item):
                    outfile.write(line[:55])
                    outfile.write('\n')
        infile.seek(0)
    outfile.write('TER\n')


def writeBindChains(bindChain,infile,outfile):
    for line in infile:
        if line.startswith('ATOM') and matchChain(line,bindChain):
            outfile.write(line[:55])
            outfile.write('\n')
    infile.seek(0)
    outfile.write('TER\n')


def enterChains():
    numRecChains = int(input("Enter number of receptor chains: "))
    print('Enter chain names one at a time, sepearated by hitting "enter"')
    recChains = []
    for i in range(0,numRecChains,1):
        chainName = input('Enter chain name: ')
        recChains.append(chainName)
    return recChains


def writeChains(infile,outfile):
    for line in infile:
            if line.startswith('ATOM'):
                if line[21] != 'A' and line[21] != 'C':
                    outfile.write(line[:21])
                    outfile.write('C')
                    outfile.write(line[22:])
                else:
                    outfile.write(line[:55])
                    outfile.write('\n')
            elif line.startswith('TER'):
                outfile.write(line[:3])
                outfile.write('\n')
            elif line.startswith('ENDMDL'):
                outfile.write('TER\n')


def main():
    batchProcessing = False
    batchInput = input("Run multiple input files? (y/n) ")
    if batchInput == 'y' or batchInput == 'Y':
        batchProcessing = True
    if not batchProcessing:
        filename = input("Enter filename to be prepared: ")
        infile = open(filename,'r')
        outfile = open("proteins.pdb",'w')
        multRecChains = input('Are there multiple receptor chains? (y/n) ')
        if multRecChains == 'y' or multRecChains == 'Y':
            recChains = enterChains()
            bindChain = input('Enter name of binding chain: ')
            writeRecChains(recChains,infile,outfile)
            writeBindChains(bindChain,infile,outfile) 
        else:
            writeChains(infile,outfile)
    else:
        fileList, fileNames = batch_processing()
        #print(fileNames)
        #print('\n')
        #print(fileList)
        for obj in fileNames:
            infile = open(fileList[obj],'r')
            outfileName = fileList[obj].rstrip('.pdb')
            if not os.path.exists(outfileName):
                os.makedirs(outfileName)
            outfileName = os.path.join(outfileName, 'proteins.pdb')
            outfile = open(outfileName, 'w')
            print(obj)
            multRecChains = input('Are there multiple receptor chains? (y/n) ')
            if multRecChains == 'y' or multRecChains == 'Y':
                recChains = enterChains()
                bindChain = input('Enter name of binding chain: ')
                writeRecChains(recChains,infile,outfile)
                writeBindChains(bindChain,infile,outfile) 
            else:
                writeChains(infile,outfile)
        
    outfile.write('END')
    infile.close()
    outfile.close()

main()
