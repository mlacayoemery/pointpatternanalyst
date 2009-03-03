"""The user interface to the class tobiiParse.

From ArcGIS use provided toolbox, or add script with parameter for input file, output dbf Table, and boolean.
Calls tobiiParse with parameters, use boolean to decide to dynamically type.
"""
__author__ = "Martin Lacayo-Emery <positrons@gmail.com>"
__date__ = "01 March 2009"

__version__ = "$Revision: 1 $"
__credits__ = """Arzu \xc7\xf6ltekin, University of Z\xfcrich, project collaborator
Sara Fabrikant, University of Z\xfcrich, project collaborator
Fulbright Program, funding agency
"""
import sys
import lib.pop.tobiiParse

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    if sys.argv[3]=="true":
        dynamicSpecs=True
    else:
        dynamicSpecs=False
    lib.pop.tobiiParse.tobiiParse(inName,outName,dynamicSpecs)