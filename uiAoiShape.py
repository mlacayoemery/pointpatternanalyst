"""Creates AOI shapes from a Tobii Studio AOI file."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import lib.shp.shapefile
import lib.shp.databasefile

def aoiShp(inName,outName,xoffset,yoffset):
    #use quadrant 4
    xScale=1
    yScale=-1
    inFile=open(inName)
    shp=lib.shp.shapefile.Shapefile(lib.shp.shapefile.shapeTypes["Polygon"])
    #make table for AOI names
    dbf=lib.shp.databasefile.DatabaseFile(["Name"],[],[])
    for l in inFile.readlines():
        #parse file line and add AOI name to table
        row=[p.split(",") for p in l.strip().split("\t")]
        dbf.addRow(row.pop(0))
        #create polygon for AOI from coordinates
        polygon=[((int(x)+xoffset)*xScale,(int(y)+yoffset)*yScale) for x,y in row]
        #close polygon and add to shapefile
        shp.add(polygon+[polygon[0]])
    #automatically detect field specs for AOI names
    dbf.dynamicSpecs()
    #add AOI names to shapefile
    shp.table.extend(dbf)
    inFile.close()
    shp.writeFile(outName)

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    xoffset=int(sys.argv[3])
    yoffset=int(sys.argv[4])
    aoiShp(inName,outName,xoffset,yoffset)
