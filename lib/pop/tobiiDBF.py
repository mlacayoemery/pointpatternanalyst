import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

headerLength=24

def tobiiParse(inName,outName,dynamicSpecs=False):
    tobiiParseFile(open(inName,'r'),open(outName,'wb'),dynamicSpecs)

def tobiiParseFile(inFile,outFile,dynamicSpecs=False):
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