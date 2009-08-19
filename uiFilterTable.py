"""The user interface for dbf filtering."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import lib.shp.databasefile

if __name__=="__main__":
    inName=sys.argv[1]
    field=sys.argv[2]
    if sys.argv[3]=="Values to Keep":
        keep=True
    else:
        keep=False
    if sys.argv[4]=="#":
        equal=None
    else:
        equal=sys.argv[4]
    if sys.argv[5]=="#":
        minimum=None
    else:
        minimum=sys.argv[5]
    if sys.argv[6]=="#":
        maximum=None
    else:
        maximum=sys.argv[6]
        
    if equal == None and minimum == None and maximum == None:
        raise ValueError, "You did not set any selection criteria. To select blank fields add a space to the equal comparison."

    outName=sys.argv[7]
    if sys.argv[8]=="true":
        retype=True
    else:
        retype=False

    #begin processing
    dbf=lib.shp.databasefile.DatabaseFile([],[],[],inName)
    dbf.select(dbf.index(field),equal,minimum,maximum,keep)
    if retype:
        dbf.dynamicSpecs()
    dbf.writeFile(outName)