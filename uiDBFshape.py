"""The user interface to the class tableToShape."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import lib.shp.tableToShape

if __name__ == "__main__":
    inName=sys.argv[1]
    xField=sys.argv[2]
    yField=sys.argv[3]
    outName=sys.argv[4]
    quadrant=sys.argv[5]
    shape=lib.shp.tableToShape.shapefile.shapeTypes[sys.argv[6]]
    if sys.argv[7]=="true":
        changeTypes=True
    else:
        changeTypes=False
        
    lib.shp.tableToShape.TableToShape(inName,xField,yField,outName,quadrant,shape,changeTypes)