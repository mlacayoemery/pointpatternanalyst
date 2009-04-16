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
    if sys.argv[4]=="#":
        scaleByField=None
    else:
        scaleByField=sys.argv[4]
    scaleUnit=float(sys.argv[5])
    aoiField=sys.argv[6]
    formatTypes=["Clustal G",
                 "State-Sequence (STS)",
                 "State-Permanence (SPS)",
                 "Distinct-State-Sequence (DSS)",
                 "Time-Stamped Event (TSE)",
                 "Person-Peroid",
                 "Shifted-Replicated-Squence (SRS)",
                 "Xbase (DBF)"]
    format=formatTypes.index(sys.argv[7])
    outName=sys.argv[8]
    aoiTable=sys.argv[9]
    aoiCodeField=sys.argv[10]
    aoiLabelField=sys.argv[11]
    
    lib.pop.SEQ.Sequence(inName,aoiField,outName,format,separateField,orderByField,scaleByField,scaleUnit,aoiTable,aoiCodeField,aoiLabelField)