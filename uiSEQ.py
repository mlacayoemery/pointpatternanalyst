"""The user interface to the SEQ."""
__author__ = "Martin Lacayo-Emery <positrons@gmail.com>"

import sys
import lib.pop.SEQ

if __name__=="__main__":
    inName=sys.argv[1]
    if sys.argv[8]=="#":
        separateField=None
    else:
        separateField=sys.argv[8]
    if sys.argv[9]=="OID":
        orderByField=None
    elif sys.argv[9]=="#":
        orderByField=None
    else:
        orderByField=sys.argv[9]
    if sys.argv[10]=="#":
        scaleByField=None
    else:
        scaleByField=sys.argv[10]
    scaleUnit=float(sys.argv[11])
    aoiField=sys.argv[2]
    formatTypes=["Clustal G",
                 "State-Sequence (STS)",
                 "State-Permanence (SPS)",
                 "Distinct-State-Sequence (DSS)",
                 "Time-Stamped Event (TSE)",
                 "Person-Peroid",
                 "Shifted-Replicated-Squence (SRS)",
                 "Xbase (DBF)"]
    format=formatTypes.index(sys.argv[6])
    outName=sys.argv[7]
    aoiTable=sys.argv[3]
    aoiCodeField=sys.argv[4]
    aoiLabelField=sys.argv[5]
    
    lib.pop.SEQ.Sequence(inName,aoiField,outName,format,separateField,orderByField,scaleByField,scaleUnit,aoiTable,aoiCodeField,aoiLabelField)