"""The batch AOIset script."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import os
import math
import string
import arcgisscripting
import lib.pop.AOIset
import lib.shp.databasefile

if __name__=="__main__":
    #create geoprocessor
    gp = arcgisscripting.create()

    #store parameters    
    inFolder=sys.argv[1]
    inName=sys.argv[2]
    fieldName=sys.argv[3]
    outName=sys.argv[6]
    label=sys.argv[4]
    if sys.argv[5]=="automatic":
        length=1
    else:
        length=int(sys.argv[5])
    valueTypes=["manual","automatic"]
    if sys.argv[7]=="#":
        value=1
    else:
        value=valueTypes.index(sys.argv[7])
    fieldX=None
    fieldY=None
    #set to no shapefile creation, or scaling
    geoType=0
    xScale=1
    yScale=1

    #create individual AOI sets and union
    AOIs=set([])
    for name in os.listdir(inFolder):
        inName=inFolder+"\\"+name
        gp.AddMessage("Processing "+inName)
        dbf=lib.shp.databasefile.DatabaseFile([],[],[],inName)
        AOIs.update(lib.pop.AOIset.AOIset(dbf,dbf.index(fieldName)))

    #convert AOIs set to list and sort        
    AOIs=list(AOIs)
    AOIs.sort()

    #construct alphabet for sequence words
    chars=string.ascii_lowercase
    #detmine minimum word length
    minimumLen=int(math.ceil(math.log(len(AOIs))/math.log(len(chars))))
    if length<minimumLen:
        #raise ValueError, "The minimum code length for your data is "+str(minimumLen)
        length=minimumLen

    #generate sequence words and store in table with AOI names
    fieldNames=[label,fieldName]
    if value==0:
        codes=[""]*len(AOIs)
    else:
        codes=lib.pop.AOIset.uniqueCodes(len(AOIs),length,chars)
    records=zip(codes,AOIs)
    aoiDBF=lib.shp.databasefile.DatabaseFile(fieldNames,[],records)
    aoiDBF.staticSpecs()
    aoiDBF.writeFile(outName)