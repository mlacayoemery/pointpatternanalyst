"""A file merging script."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import os
import arcgisscripting

if __name__=="__main__":
    #create geoprocessor object
    gp = arcgisscripting.create()

    #store parameters    
    inFolder=sys.argv[1]
    outName=sys.argv[2]
    if sys.argv[3]=="true":
        header=True
    else:
        header=False
        
    outFile=open(outName,"w")

    #if file header, pick longest
    finalHeader=""
    if header:
        gp.addwarning("The longest header is being selected for the final ouput.")
        for name in os.listdir(inFolder):
            inName=inFolder+"\\"+name
            inFile=open(inName)
            tempHeader=inFile.readline()
            if len(tempHeader)>len(finalHeader):
                finalHeader=tempHeader
            inFile.close()
        outFile.write(finalHeader)

    #read in each file and write to output
    for name in os.listdir(inFolder):
        inName=inFolder+"\\"+name
        gp.AddMessage("Processing "+inName)
        inFile=open(inName)
        #skip header line if present
        if header:
            inFile.readline()
        #end each sequence with a end of line, otherwise TraMineR parse warnings
        outFile.write(inFile.read().strip()+"\n")
        inFile.close()
        
    outFile.close()