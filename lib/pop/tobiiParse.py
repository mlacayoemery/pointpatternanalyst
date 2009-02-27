import sys
from ..shp import databasefile

headerLength=24

def tobiiParseFile(inName,outName,dynamicSpecs=False):
    tobiiParse(open(inName,'r'),open(outName,'wb'),dynamicSpecs)

def tobiiParse(inFile,outFile,dynamicSpecs=False):
    #read in file, remove header, strip and split lines
    lines=[l.replace("\t\n","\n").split("\t") for l in inFile.readlines()[headerLength:]]
    inFile.close()
    header=lines.pop(0)
    
    d=databasefile.DatabaseFile(header,None,lines)
    if dynamicSpecs:
        d.dynamicSpecs()
    else:
        d.staticSpecs()
    d.write(outFile)