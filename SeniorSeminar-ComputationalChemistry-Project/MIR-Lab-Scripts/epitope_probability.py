from statistics import *

class stats:
    stdeviation = 0
    average = 0
    vals = []
    
    def __init__(self, values):
        self.vals = values
        self.stdeviation = pstdev(values)
        total = float(0)
        for pos in range(len(values)):
            #print(pos)
            total += values[pos]
        self.average = total / float(len(values))

        
def readFile(infile):
    vals = []
    for line in infile:
        stringVals = line[-6:]
        #print(stringVals)
        floatVals = float(stringVals)
        #print(floatVals)
        vals.append(floatVals)
    return vals

def writeFile(outfile, data, filename):
    outfile.write("Average Probability of Residues for ")
    outfile.write(filename)
    outfile.write("\n")
    outfile.write("Number of residues: ")
    outfile.write(str(len(data.vals)))
    outfile.write("\n")
    outfile.write("Average is: ")
    outfile.write(str(data.average))
    outfile.write("\n")
    outfile.write("stdev is: ")
    outfile.write(str(data.stdeviation))
    outfile.write("\n")


def main():
    infileName = input("Input .pdb file to read (include .pdb): ")
    outfileName = input("Input name of outfile (include .txt): ")
    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')

    vals = readFile(infile)
    data = stats(vals)

    writeFile(outfile, data, infileName)

    infile.close()
    outfile.close()


main()

    
