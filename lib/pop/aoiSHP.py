from ..shp import shapefile
from ..shp import databasefile

def aoiShp(inName,outName):
    inFile=open(inName)
    shp=shapefile(shapefile.shapeTypes["Polygon"])
    aoiShpFile(inFile,shp)
    inFile.close()
    shp.write(outName)

def aoiShpFile(inFile,shp):
    dbf=databasefile(["Name"],[],[])
    for l in inFile.readlines():
        row=l.split("\t")
        dbf.addRpw([row.pop(0)])
        shp.add(map(",".split,row))
    dbf.dynamicSpecs()
    shp.extend(dbf)    
    
        
            
    