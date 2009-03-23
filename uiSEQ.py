"""The user interface to the SEQ.
"""
__author__ = "Martin Lacayo-Emery <positrons@gmail.com>"
__date__ = "09 March 2009"

__version__ = "$Revision: 1 $"
__credits__ = """Arzu \xc7\xf6ltekin, University of Z\xfcrich, project collaborator
Sara Fabrikant, University of Z\xfcrich, project collaborator
Fulbright Program, funding agency
"""
import sys
import lib.pop.SEQ

if __name__=="__main__":
    inName=sys.argv[1]
    if sys.argv[2]=="#":
        separateField=None
    else:
        separateField=sys.argv[2]
    if sys.argv[3]=="OID":
        orderByField=None
    elif sys.argv[3]=="#":
        orderByField=None
    else:
        orderByField=sys.argv[3]
    aoiField=sys.argv[4]
    scaleByField=None
    format=None
    outName=sys.argv[5]
    aoiTable=sys.argv[6]
    aoiCodeField=sys.argv[7]
    aoiLabelField=sys.argv[8]
    
    lib.pop.SEQ.Sequence(inName,aoiField,outName,format,separateField,orderByField,aoiTable,aoiCodeField,aoiLabelField)