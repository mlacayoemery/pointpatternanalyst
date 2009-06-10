"""Parses the Tobii Studio"""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"
import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

def tobiiParse(inName,outName,dynamicSpecs=False):
    tobiiParseFile(open(inName,'r'),open(outName,'wb'),dynamicSpecs)

def tobiiParseFile(inFile,outFile,dynamicSpecs=False):
    #read in file, remove header, strip and split lines
    lines=inFile.readlines()
    inFile.close()
    lines.reverse()
    lines=lines[:lines.index("\n")]
    lines.reverse()
    lines=[l.replace("\t\n","").split("\t") for l in lines]
    header=lines.pop(0)
    
    d=databasefile.DatabaseFile(header,None,lines)
    if dynamicSpecs:
        d.dynamicSpecs()
    else:
        d.staticSpecs()
    d.write(outFile)