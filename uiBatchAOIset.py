"""The user interface to the scripts in AOIset.

From ArcGIS use provided toolbox, or add script with parameters for the input dbf file,
the field name, and ouput text file.

Calls AOIsetFile with parameters.
"""
__author__ = "Martin Lacayo-Emery <positrons@gmail.com>"
__date__ = "05 March 2009"

__version__ = "$Revision: 1 $"
__credits__ = """Arzu \xc7\xf6ltekin, University of Z\xfcrich, project collaborator
Sara Fabrikant, University of Z\xfcrich, project collaborator
University of Z\xfcrich, host institution
Fulbright Program, funding agency
"""

import sys
import os
import math
import string
import arcgisscripting
import lib.pop.AOIset
import lib.shp.databasefile

if __name__=="__main__":
    gp = arcgisscripting.create()
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
    geoType=0
    xScale=1
    yScale=1

    AOIs=set([])
    for name in os.listdir(inFolder):
        inName=inFolder+"\\"+name
        gp.AddMessage("Processing "+inName)
        dbf=lib.shp.databasefile.DatabaseFile([],[],[],inName)
        AOIs.update(lib.pop.AOIset.AOIset(dbf,dbf.index(fieldName)))
        
    AOIs=list(AOIs)
    AOIs.sort()

    chars=string.ascii_lowercase
    minimumLen=int(math.ceil(math.log(len(AOIs))/math.log(len(chars))))
    if length<minimumLen:
        #raise ValueError, "The minimum code length for your data is "+str(minimumLen)
        length=minimumLen

    fieldNames=[label,fieldName]
    if value==0:
        codes=[""]*len(AOIs)
    else:
        codes=lib.pop.AOIset.uniqueCodes(len(AOIs),length,chars)
    records=zip(codes,AOIs)
    aoiDBF=lib.shp.databasefile.DatabaseFile(fieldNames,[],records)
    aoiDBF.staticSpecs()
    aoiDBF.writeFile(outName)
