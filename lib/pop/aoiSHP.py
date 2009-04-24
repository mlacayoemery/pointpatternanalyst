import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import shapefile
import databasefile

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
    
        
            
    