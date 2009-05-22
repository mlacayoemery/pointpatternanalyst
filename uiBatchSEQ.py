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
import os
import arcgisscripting
import lib.pop.SEQ

if __name__=="__main__":
    gp = arcgisscripting.create(9.3)

    inFolder=sys.argv[1]
    inName=sys.argv[2]
    aoiField=sys.argv[3]
    aoiTable=sys.argv[4]
    aoiCodeField=sys.argv[5]
    aoiLabelField=sys.argv[6]

    formatTypes=["Clustal G",
                 "State-Sequence (STS)",
                 "State-Permanence (SPS)",
                 "Distinct-State-Sequence (DSS)",
                 "Time-Stamped Event (TSE)",
                 "Person-Peroid",
                 "Shifted-Replicated-Squence (SRS)",
                 "Xbase (DBF)"]
    print sys.argv[7]
    format=formatTypes.index(sys.argv[7])
    outFolder=sys.argv[8]

    if sys.argv[9]=="#":
        separateField=None
    else:
        separateField=sys.argv[9]
    if sys.argv[10]=="OID":
        orderByField=None
    elif sys.argv[10]=="#":
        orderByField=None
    else:
        orderByField=sys.argv[10]
    if sys.argv[11]=="#":
        scaleByField=None
    else:
        scaleByField=sys.argv[11]
    if sys.argv[12]=="#":
        scaleUnit=1
    else:
        scaleUnit=float(sys.argv[12])

    for name in os.listdir(inFolder):
        inName=inFolder+"\\"+name
        outName=outFolder+"\\"+name.replace(".","_")+".txt"
        gp.AddMessage("Processing "+inName)     
        lib.pop.SEQ.Sequence(inName,aoiField,outName,format,separateField,orderByField,scaleByField,scaleUnit,aoiTable,aoiCodeField,aoiLabelField)
    