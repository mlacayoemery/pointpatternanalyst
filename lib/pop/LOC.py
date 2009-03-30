from ..shp import databasefile

def locFile(aoisName,aoisField,priorityField,xField,yField,aoisetName,aoisetField,aoicodeField,outName):
    if aoisName[aoisName.rfind("."):]==".shp":
        aois=databasefile.DatabaseFile([],[],[],aoisName[:aoisName.rfind(".")]+".dbf")
    else:
        aois=databasefile.DatabaseFile([],[],[],aoisName)
    aoiset=databasefile.DatabaseFile([],[],[],aoisetName)

    aoisIndex=aois.index(aoisField)
    priorityIndex=aois.index(priorityField)
    xIndex=aois.index(xField)
    yIndex=aois.index(yField)
    aoisetIndex=aoiset.index(aoisetField)
    aoicodeIndex=aoiset.index(aoicodeField)
    
    outFile=open(outName,"w")
    for row in aoiset:
        candidates=row[aoisetIndex].split(",")
        try:
            match=aois.find(aoisIndex,candidates.pop())        
            for name in candidates:
                temp=aois.find(aoisIndex,name)
                if float(aois[temp][priorityIndex])<float(aois[match][priorityIndex]):
                    match=temp
        except ValueError,i:
            raise ValueError, "The is an AOI named"+i+"in the set table that is not other table."
        
        outFile.write("seqID "+row[aoicodeIndex]+"   1  "+aois[match][xIndex]+"     "+aois[match][yIndex]+"\n")
    outFile.close()