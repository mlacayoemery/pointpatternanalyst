import sys
import os

inFileName = sys.argv[1]
outFileName = sys.argv[2]

inFile = open(inFileName)
outFile = open(outFileName, 'w')

line = ""

while line != "##":
    line = inFile.readline().strip()

#header
inFile.readline()
#message
start = int(inFile.readline().strip().split("\t")[0])

outFile.write("\n" * 18)
outFile.write("\nTimestamp\tStimuliName\tAoiNames\tGazePointX\tGazePointY\tFixationDuration")

for line in inFile:
    line = line.strip().split("\t")
    outFile.write("\n"+"\t".join([line[0],line[11],line[7],line[3],line[4],str(int(line[0])-start)]))
    start = int(line[0])

inFile.close()
outFile.close()
