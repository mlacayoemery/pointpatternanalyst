import sys

def tobiiParse(inName,outName):
    inFile=open(inName)
    outFile=open(outName,'w')
    lines=inFile.readlines()
    outFile.write(''.join(lines[24:]).replace("\t",",").replace("\r",""))
    inFile.close()
    outFile.close()

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    tobiiParse(inName,outName)