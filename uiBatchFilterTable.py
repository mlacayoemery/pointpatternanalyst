"""The batch filter script"""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import os
import arcgisscripting
import lib.shp.databasefile

if __name__=="__main__":
    #create geoprocessor
    gp = arcgisscripting.create()

    #store parameters    
    inFolder=sys.argv[1]
    inName=sys.argv[2]
    field=sys.argv[3]
    if sys.argv[4]=="Values to Keep":
        keep=True
    else:
        keep=False
    if sys.argv[5]=="#":
        equal=None
    else:
        equal=sys.argv[5]
    if sys.argv[6]=="#":
        minimum=None
    else:
        minimum=sys.argv[6]
    if sys.argv[7]=="#":
        maximum=None
    else:
        maximum=sys.argv[7]
        
    if equal == None and minimum == None and maximum == None:
        raise ValueError, "You did not set any selection criteria. To select blank fields add a space to the equal comparison."
        
    outFolder=sys.argv[8]
    if sys.argv[9]=="true":
        retype=True
    else:
        retype=False

    #loop over each file in directory, perform filter        
    for name in os.listdir(inFolder):
        inName=inFolder+"\\"+name
        outName=outFolder+"\\"+name
        gp.AddMessage("Processing "+inName)        
        dbf=lib.shp.databasefile.DatabaseFile([],[],[],inName)
        dbf.select(dbf.index(field),equal,minimum,maximum,keep)
        if retype:
            dbf.dynamicSpecs()
        dbf.writeFile(outName)
