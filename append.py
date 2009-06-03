import sys
import os
import arcgisscripting

if __name__=="__main__":
    gp = arcgisscripting.create()
    
    inFolder=sys.argv[1]
    outName=sys.argv[2]
    if sys.argv[3]=="true":
        header=True
    else:
        header=False
        
    outFile=open(outName,"w")

    finalHeader=""
    if header:
        for name in os.listdir(inFolder):
            inName=inFolder+"\\"+name
            inFile=open(inName)
            tempHeader=inFile.readline()
            if len(tempHeader)>len(finalHeader):
                finalHeader=tempHeader
            inFile.close()
        outFile.write(finalHeader)
        
    for name in os.listdir(inFolder):
        inName=inFolder+"\\"+name
        gp.AddMessage("Processing "+inName)
        inFile=open(inName)
        if header:
            inFile.readline()
        outFile.write(inFile.read().strip()+"\n")
        inFile.close()
        
    outFile.close()