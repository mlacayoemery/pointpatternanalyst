"""The user interface to the class animeyeParse."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import lib.pop.animeyeDBF

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    dynamicSpecs=sys.argv[3]
    lib.pop.animeyeDBF.animeyeParse(inName,outName,dynamicSpecs)