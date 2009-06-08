"""The user interface for dbf filtering."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import lib.shp.dbfFilter

if __name__=="__main__":
    inName=sys.argv[1]
    field=sys.argv[2]
    if sys.argv[3]=="Values to Keep":
        keep=True
    else:
        keep=False
    equal=sys.argv[4]
    minimum=sys.argv[5]
    maximum=sys.argv[6]
    if equal == "#" and minimum == "#" and maximum == "#":
        raise ValueError, "You did not set any selection criteria. To select blank fields add a space to the equal comparison."
    outName=sys.argv[7]
    if sys.argv[8]=="true":
        retype=True
    else:
        retype=False
    lib.shp.dbfFilter.filterTable(inName,outName,field,keep,equal,minimum,maximum,retype)