"""The batch filter script"""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import os
import arcgisscripting
import lib.shp.dbfFilter

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
    equal=sys.argv[5]
    minimum=sys.argv[6]
    maximum=sys.argv[7]
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
        lib.shp.dbfFilter.filterTable(inName,outName,field,keep,equal,minimum,maximum,retype)
