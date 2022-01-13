'''
*** ZDOCK Fix v1.1
*** Author: Colin Welsh
*** Date Created: 19 June 2017
'''

import os


### Purpose: Removes information from each line that prevents .pdb file from being opened in Chimera
### Parameters: filePrefixAntigen, the the name of the antigen;
###             filePrefixCap, the name of the cap
### Returns: outNames, a list of the outputted .pdb files that are compatible with Chimera
def zdock_to_chimera(filePrefixAntigen, filePrefixCap):
    cnt = 1
    fileNames = []
    outNames = []
    for i in range(1,11,1):
        name = "complex." + str(i) + ".pdb"
        fileNames.append(name)
    for obj in fileNames:
        infile = open(obj, 'r')
        outName = "zdock_" + filePrefixAntigen + "_" + filePrefixCap + "_complex" + str(cnt) + ".pdb"
        outNames.append(outName)
        outfile = open(outName, 'w')
        cnt += 1
        for line in infile:
            line = line.rstrip('\n')
            info = line[0:55]
            outfile.write(info)
            outfile.write('\n')
        infile.close()
        outfile.close()
    return outNames


### Purpose: Creates the file directory in which proteins.pdb files are placed
### Parameters: dirList, the list of directories to create
### Returns: None
def make_dir(dirList):
    cnt = 0
    for obj in dirList:
        os.makedirs(dirList[cnt])
        cnt += 1


### Purpose: Creates the list of directories to be created for the proteins.pdb files
### Parameters: fileRoot, the location of zdock_fix.py;
###             fileNames, the list of Chimera-compatible .pdb files;
###             antiName, the name of the Antigen
###             capName, the name of the protein cap;
### Returns: dirList, the list of directories to be created
def make_dir_list(fileRoot, fileNames, antiName, capName):
    dirList = []
    cnt = 0
    newFolder = antiName + '_' + capName + '_ROSIE_files'
    for obj in fileNames:
        newDir = os.path.join(fileRoot,newFolder,fileNames[cnt].rstrip('.pdb'))
        dirList.append(newDir)
        cnt += 1
    return dirList


### Purpose: Converts Chimera-ready .pdb files into the appropriate format for ROSIE
### Parameters: dirList, the list of the directories to place proteins.pdb files in
###             fileNames, list of files to be converted into the appropriate ROSIE format
### Returns: None
def convert_to_rosie(dirList,fileNames):
    cnt = 0
    for obj in fileNames:
        infile = open(fileNames[cnt],'r')
        outName = os.path.join(dirList[cnt],'proteins.pdb')
        outfile = open(outName,'w')
        prevNum = 0
        for line in infile:
            line = line.rstrip('\n')
            num = line[23:26]
            num = int(num.lstrip('  '))
            if num < prevNum:
                outfile.write('TER\n')
            if line.startswith('ATOM'):
                if line[21] != 'A' or line[21] != 'C':
                    outfile.write(line[:21])
                    outfile.write('C')
                    outfile.write(line[22:])
                    outfile.write('\n')
                else:
                    outfile.write(line[:55])
                    outfile.write('\n')
                
            elif line.startswith('TER'):
                outfile.write(line[:2])
                outfile.write('\n')
            elif line.startswith('ENDMDL'):
                outfile.write('TER\n')
            prevNum = num
        outfile.write('END')
        infile.close()
        outfile.close()
        cnt += 1


def main():
    fileRoot = os.getcwd()
    print(fileRoot)
    antiName = input("Enter antigen name: ")
    capName = input("Enter cap name: ")
    fileNames = zdock_to_chimera(antiName, capName)
    dirList = make_dir_list(fileRoot, fileNames, antiName, capName)
    make_dir(dirList)
    convert_to_rosie(dirList,fileNames)

main()
