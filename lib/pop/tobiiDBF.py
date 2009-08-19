"""Parses the Tobii Studio"""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"
import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

def tobiiParseFile(inName,outName,dynamicSpecs=False):
    tobiiParse(open(inName,'r'),open(outName,'wb'),dynamicSpecs)

def tobiiParse(inFile,outFile,dynamicSpecs=False):
    #read in file, remove header, strip and split lines
    lines=inFile.read().strip()
    inFile.close()
    #use last end of line delimted block for table
    blockIndex=lines.rfind("\n\n")
    if blockIndex != -1:
        lines=lines[blockIndex+2:].split("\t\n")
    else:
        lines=lines.split("\t\n")
    lines=[l.split("\t") for l in lines]
    header=lines.pop(0)
    d=databasefile.DatabaseFile(header,None,[])
    width=len(header)
    for l in lines:
        d.addRow(l+((width-len(l))*[""]))
        
    if dynamicSpecs:
        d.dynamicSpecs()
    else:
        d.staticSpecs()
    d.write(outFile)

if __name__=="__main__":
    tobiiParseFile(sys.argv[1],sys.argv[2])