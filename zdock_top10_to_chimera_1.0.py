'''
*** ZDock to Chimera Converter v1.0
*** Author: Colin Welsh
*** Date Created: 15 February 2017
'''

def main():
    filenames = []
    filePrefixAntigen = input("Enter Antigen name: ")
    filePrefixCap = input("Enter Cap name: ")
    for i in range(1,11,1):
        name = "complex." + str(i) + ".pdb"
        filenames.append(name)
    for obj in filenames:
        infile = open(obj, 'r')
        outName = "zdock_" + filePrefixAntigen + "_" + filePrefixCap + "_complex" + str(cnt) + ".pdb"
        outfile = open(outName, 'w')
        for line in infile:
            line = line.rstrip('\n')
            info = line[0:55]
            outfile.write(info)
            outfile.write('\n')
        infile.close()
        outfile.close()

main()
