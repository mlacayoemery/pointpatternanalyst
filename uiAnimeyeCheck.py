"""The user interface to the class animeyeCheck."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import lib.pop.animeyeCheck

if __name__=="__main__":
    inName=sys.argv[1]
    outReport=sys.argv[2]
    if sys.argv[3] == "#":
        outName=None
    else:
        outName=sys.argv[3]
    if sys.argv[4]=="true":
        verbose=True
    else:
        verbose=False

    lib.pop.animeyeCheck.animeyeCheck(inName,outReport,outName,verbose)
