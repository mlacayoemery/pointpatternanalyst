"""Creates the location file for a sequence"""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"
import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

def locFile(aoisName,aoisField,priorityField,xField,yField,aoisetName,aoisetField,aoicodeField,outName):
    #create files
    if aoisName[aoisName.rfind("."):]==".shp":
        aois=databasefile.DatabaseFile([],[],[],aoisName[:aoisName.rfind(".")]+".dbf")
    else:
        aois=databasefile.DatabaseFile([],[],[],aoisName)
    aoiset=databasefile.DatabaseFile([],[],[],aoisetName)

    #get table column indicies
    aoisIndex=aois.index(aoisField)
    priorityIndex=aois.index(priorityField)
    xIndex=aois.index(xField)
    yIndex=aois.index(yField)
    aoisetIndex=aoiset.index(aoisetField)
    aoicodeIndex=aoiset.index(aoicodeField)

    #read table and write coordinates to a location file    
    outFile=open(outName,"w")
    for row in aoiset:
        candidates=row[aoisetIndex].split(",")
        try:
            match=aois.find(aoisIndex,candidates.pop())        
            for name in candidates:
                temp=aois.find(aoisIndex,name)
                #use a priority field to choose which coordintates to use
                if float(aois[temp][priorityIndex])<float(aois[match][priorityIndex]):
                    match=temp
        except ValueError,i:
            raise ValueError, "The AOI named"+i+" is not in the set table."
        
        outFile.write("seqID "+row[aoicodeIndex]+"   1  "+aois[match][xIndex]+"     "+aois[match][yIndex]+"\n")
    outFile.close()