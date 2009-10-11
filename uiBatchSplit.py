__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import os
import arcgisscripting
import lib.pop.separate

if __name__=="__main__":
    #create geoprocessor object
    gp = arcgisscripting.create()

    #store parameters
    inFolder=sys.argv[1]
    fieldName=sys.argv[3]
    outFolder=sys.argv[4]
    if sys.argv[5]=="true":
        stemname=True
    else:
        stemname=False
    namingSchemeValues=["Value","Order"]
    namingScheme=namingSchemeValues.index(sys.argv[6])


    for name in os.listdir(inFolder):
        inName=inFolder+"\\"+name
        gp.AddMessage("Spliting "+inName)
        if stemname:
            stem=name.replace(".","_")+".dbf"
        else:
            stem=""
        lib.pop.separate.separateFile(inName,fieldName,outFolder,stem,namingScheme)