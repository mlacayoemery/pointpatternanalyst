import sys
import os
import arcgisscripting

if __name__=="__main__":
    gp = arcgisscripting.create()
    
    inFolder=sys.argv[1]
    outName=sys.argv[2]
    outFile=open(outName,"w")
    
    for name in os.listdir(inFolder):
        inName=inFolder+"\\"+name
        gp.AddMessage("Processing "+inName)
        inFile=open(inName)
        outFile.write(inFile.read()+"\n")
        inFile.close()
        
    outFile.close()
 