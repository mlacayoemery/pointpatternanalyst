"""The user interface to the class animeyeCheck.

From ArcGIS use provided toolbox, or add script with parameters for the input tsv file,
output text report file, and the optional corrected tsv file.

Calls animeyeCheck with parameters.
"""
__author__ = "Martin Lacayo-Emery <positrons@gmail.com>"
__date__ = "03 March 2009"

__version__ = "$Revision: 1 $"
__credits__ = """Arzu \xc7\xf6ltekin, University of Z\xfcrich, project collaborator
Sara Fabrikant, University of Z\xfcrich, project collaborator
University of Z\xfcrich, host institution
Fulbright Program, funding agency
"""

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
