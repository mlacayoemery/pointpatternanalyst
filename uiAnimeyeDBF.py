"""The user interface to the class animeyeParse.

From ArcGIS use provided toolbox, or add script with parameters for the input file,
output dbf table, and boolean.

Calls animeyeParse with parameters.
"""
__author__ = "Martin Lacayo-Emery <positrons@gmail.com>"
__date__ = "01 March 2009"

__version__ = "$Revision: 1 $"
__credits__ = """Arzu \xc7\xf6ltekin, University of Z\xfcrich, project collaborator
Sara Fabrikant, University of Z\xfcrich, project collaborator
Fulbright Program, funding agency
"""
import sys
import lib.pop.animeyeParse

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    dynamicSpecs=sys.argv[3]
    lib.pop.animeyeParse.animeyeParse(inName,outName,dynamicSpecs)