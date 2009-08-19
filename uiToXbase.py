"""The inteface script for parsing."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"
import sys

if __name__=="__main__":
    inName=sys.argv[1]
    conversionType=sys.argv[2]
    outName=sys.argv[3]
    if sys.argv[4]=="true":
        dynamicSpecs=True
    else:
        dynamicSpecs=False
    if conversionType=="Tab Separated Values (TSV)":
        #add absolute path for shapefile library (relative to file import)
        sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
        import databasefile
        dbf=databasefile.DatabaseFile([],[],[])
        dbf.readTSV(inName)
        if dynamicSpecs:
            dbf.dynamicSpecs()
        dbf.writeFile(outName)
    elif conversionType=="Tobii TSV with Header":
        import lib.pop.tobiiDBF
        lib.pop.tobiiDBF.tobiiParseFile(inName,outName,dynamicSpecs)
    elif conversionType=="SMI TSV with Multiple Areas of Interest":
        import lib.pop.animeyeDBF
        lib.pop.animeyeDBF.animeyeParse(inName,outName,dynamicSpecs,multipleAOIs)
    else:
        raise ValueError, conversionType + " is not a defined format."
