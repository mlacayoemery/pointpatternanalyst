import sys
import os
import arcgisscripting

if __name__=="__main__":
    gp = arcgisscripting.create()

    inFolder=sys.argv[1]
    conversionType=sys.argv[2]
    outFolder=sys.argv[3]
    if sys.argv[4]=="true":
        dynamicSpecs=True
    else:
        dynamicSpecs=False
    if conversionType=="Tobii":
        import lib.pop.tobiiDBF
        for name in os.listdir(inFolder):
            inName=inFolder+"\\"+name
            outName=outFolder+"\\"+name.replace(".","_")+".dbf"
            gp.AddMessage("Converting "+inName)
            lib.pop.tobiiDBF.tobiiParse(inName,outName,dynamicSpecs)
    elif conversionType=="SensoMotoric":
        import lib.pop.animeyeDBF
        for name in os.listdir(inFolder):
            inName=inFolder+"\\"+name
            outName=outFolder+"\\"+name.replace(".","_")+".dbf"
            gp.AddMessage("Converting "+inName)
            lib.pop.animeyeDBF.animeyeParse(inName,outName,dynamicSpecs)
    else:
        raise ValueError, conversionType + " is not a defined format."
