import sys, databasefile

def tobiiParse(inName,outName):
    headerLength=24
    #read in file, remove header, strip and split lines
    inFile=open(inName)
    lines=inFile.readlines()[headerLength:]
    inFile.close()
    header=lines.pop(0).strip().split("\t")
    lines=[l.split("\t") for l in lines]
            
    d=databasefile.DatabaseFile(header,None,lines)
    d.refreshSpecs()
    d.writeFile(outName)    

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    tobiiParse(inName,outName)