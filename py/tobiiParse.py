import sys
import databasefile

def tobiiParse(inName,outName,dynamicSpecs):
    headerLength=24
    #read in file, remove header, strip and split lines
    inFile=open(inName)
    lines=inFile.readlines()[headerLength:]
    inFile.close()
    header=lines.pop(0).strip().split("\t")
    lines=[l.split("\t") for l in lines]
            
    d=databasefile.DatabaseFile(header,None,lines)
    if dynamicSpecs=="true":
        d.dynamicSpecs()
    else:
        d.staticSpecs()
    d.writeFile(outName)    

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    dynamicSpecs=sys.argv[3]
    tobiiParse(inName,outName,dynamicSpecs)