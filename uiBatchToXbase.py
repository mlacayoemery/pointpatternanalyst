"""The batch to Xbase script."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import os
import arcgisscripting

if __name__=="__main__":
    #create geoprocessor object
    gp = arcgisscripting.create()

    #store parameters
    inFolder=sys.argv[1]
    conversionType=sys.argv[2]
    outFolder=sys.argv[3]
    if sys.argv[4]=="true":
        dynamicSpecs=True
    else:
        dynamicSpecs=False

    #import and run type specific conversion for each file in folder
    if conversionType=="Tobii":
        import lib.pop.tobiiDBF
        for name in os.listdir(inFolder):
            inName=inFolder+"\\"+name
            #remove dot from name, as ArcGIS doesn't like it
            outName=outFolder+"\\"+name.replace(".","_")+".dbf"
            gp.AddMessage("Converting "+inName)
            lib.pop.tobiiDBF.tobiiParseFile(inName,outName,dynamicSpecs)
    elif conversionType=="SensoMotoric":
        import lib.pop.animeyeDBF
        for name in os.listdir(inFolder):
            inName=inFolder+"\\"+name
            #remove dot from name, as ArcGIS doesn't like it
            outName=outFolder+"\\"+name.replace(".","_")+".dbf"
            gp.AddMessage("Converting "+inName)
            lib.pop.animeyeDBF.animeyeParse(inName,outName,dynamicSpecs)
    else:
        raise ValueError, conversionType + " is not a defined format."
