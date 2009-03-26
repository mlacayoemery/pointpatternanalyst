"""The user interface to the class tableToShape.

From ArcGIS use provided toolbox, or add script with parameters for the input dbf file,
x field, y field, output shapefile, Cartesian quadrant, shape type (point or line),
and dynamically type boolean.

Calls tableToShape with parameters.
"""
__author__ = "Martin Lacayo-Emery <positrons@gmail.com>"
__date__ = "01 March 2009"

__version__ = "$Revision: 1 $"
__credits__ = """Arzu \xc7\xf6ltekin, University of Z\xfcrich, project collaborator
Sara Fabrikant, University of Z\xfcrich, project collaborator
Fulbright Program, funding agency
"""

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