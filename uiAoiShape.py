import sys
import lib.shp.shapefile
import lib.shp.databasefile

def aoiShp(inName,outName):
    xScale=1
    yScale=-1
    inFile=open(inName)
    shp=lib.shp.shapefile.Shapefile(lib.shp.shapefile.shapeTypes["Polygon"])
    dbf=lib.shp.databasefile.DatabaseFile(["Name"],[],[])
    for l in inFile.readlines():
        row=[p.split(",") for p in l.strip().split("\t")]
        dbf.addRow(row.pop(0))
        polygon=[(int(x)*xScale,int(y)*yScale) for x,y in row]
        shp.add(polygon+[polygon[0]])
    dbf.dynamicSpecs()
    shp.table.extend(dbf)
    inFile.close()
    shp.writeFile(outName)

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    aoiShp(inName,outName)