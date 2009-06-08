"""The user interface to the scripts in AOIset."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import lib.pop.AOIset

if __name__=="__main__":
    inName=sys.argv[1]
    fieldName=sys.argv[2]
    outName=sys.argv[5]
    label=sys.argv[3]
    if sys.argv[4]=="automatic":
        length=1
    else:
        length=int(sys.argv[4])
    valueTypes=["manual","automatic"]
    if sys.argv[6]=="#":
        value=1
    else:
        value=valueTypes.index(sys.argv[6])
    fieldX=None
    fieldY=None
    geoType=0
    xScale=1
    yScale=1
    if len(sys.argv)==11:
        fieldX=sys.argv[7]
        fieldY=sys.argv[8]
        geoTypes=["bounding box"]
        geoType=geoTypes.index(sys.argv[9])
        scaleTypes=[(1,1),(-1,1),(-1,-1),(1,-1)]
        xScale,yScale=scaleTypes[int(sys.argv[10])-1]
        
    lib.pop.AOIset.AOIsetFile(inName,outName,fieldName,label,length,value,fieldX,fieldY,geoType,xScale,yScale)
