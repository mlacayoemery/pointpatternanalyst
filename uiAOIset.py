"""The user interface to the scripts in AOIset.

From ArcGIS use provided toolbox, or add script with parameters for the input dbf file,
the field name, and ouput text file.

Calls AOIsetFile with parameters.
"""
__author__ = "Martin Lacayo-Emery <positrons@gmail.com>"
__date__ = "05 March 2009"

__version__ = "$Revision: 1 $"
__credits__ = """Arzu \xc7\xf6ltekin, University of Z\xfcrich, project collaborator
Sara Fabrikant, University of Z\xfcrich, project collaborator
University of Z\xfcrich, host institution
Fulbright Program, funding agency
"""

import sys
import lib.pop.AOIset

if __name__=="__main__":
    inName=sys.argv[1]
    fieldName=sys.argv[2]
    outName=sys.argv[3]
    label=sys.argv[4]
    length=int(sys.argv[5])
    valueTypes=["manual","automatic"]
    value=valueTypes.index(sys.argv[6])
    fieldX=None
    fieldY=None
    geoType=0
    if len(sys.argv)==10:
        fieldX=sys.argv[7]
        fieldY=sys.argv[8]
        geoTypes=["bounding box"]
        geoType=geoTypes.index(sys.argv[9])
        
    lib.pop.AOIset.AOIsetFile(inName,outName,fieldName,label,length,value,fieldX,fieldY,geoType)
