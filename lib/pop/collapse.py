"""The script that parses Tobii AOI files"""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"
import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

def CollapseFile(inName,collapseField,defaultOperation,outName,minimumFields,meanFields,medianFields,maximumFields,sumFields):
    inTable=databasefile.DatabaseFile([],[],[],inName)
    outTable=databasefile.DatabaseFile(inTable.fieldnames,inTable.fieldspecs,[])
    Collapse(inTable,collapseField,defaultOperation,outTable,minimumFields,meanFields,medianFields,maximumFields,sumFields)
    outTable.writeFile(outname)

def Collapse(inTable,collapseField,defaultOperation,outTable,minimumFields,meanFields,medianFields,maximumFields,sumFields):
    tempTable=databasefile.DatabaseFile(inTable.fieldnames,inTable.fieldspecs,inTable[0])
    collapseFieldIndex=inTable.index(collapseField)
    for i in range(1,len(inTable)):
        if inTable[i][collapseFieldIndex]==tempTable[0][collapseFieldIndex]:
            inTable.addRow(inTable[i])
        else:
            
