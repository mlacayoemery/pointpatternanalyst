"""Split DBFs into multiple fields."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import os
import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

def separateFile(dbfName,fieldName,folder,stem,namingScheme):
    dbf=databasefile.DatabaseFile([],[],[],dbfName)
    fieldIndex=dbf.index(fieldName)
    files=separate(dbf,fieldIndex,stem,namingScheme)

    #make output directory if it does not exist
    if not os.path.isdir(folder):
        os.mkdir(folder)
    for name,dbf in files:
        dbf.writeFile(folder+"\\"+name+".dbf")

def separate(dbf,fieldIndex,stem,namingScheme):
    d={}
    n=[]
    for row in dbf:
        id=row[fieldIndex]
        if d.has_key(id):
            d[id].addRow(row)
        else:
            n.append(id)
            d[id]=databasefile.DatabaseFile(dbf.fieldnames,dbf.fieldspecs,[row])
    results=[]
    if namingScheme==0:
        for id in n:
            results.append((stem+id.strip(),d[id]))
    else:
        for i,id in enumerate(n):
            results.append((stem+str(i),d[id]))
    return results
        