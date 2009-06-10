"""The user interface to the class tobiiParse."""
__author__ = "Martin Lacayo-Emery <positrons@gmail.com>"

import sys
import lib.pop.tobiiDBF

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    if sys.argv[3]=="true":
        dynamicSpecs=True
    else:
        dynamicSpecs=False
    lib.pop.tobiiDBF.tobiiParse(inName,outName,dynamicSpecs)